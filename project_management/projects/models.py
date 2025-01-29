from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    """
    Расширенная модель пользователя с добавлением ролей.
    """
    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('manager', 'Менеджер проекта'),
        ('executor', 'Исполнитель'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='executor',
        verbose_name='Роль'
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class Project(models.Model):
    """
    Модель проекта с информацией о статусе, менеджере, исполнителе и описании.
    """
    STATUS_CHOICES = [
        ('active', 'Активный'),
        ('completed', 'Завершен'),
        ('paused', 'Приостановлен'),
    ]

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name='Статус'
    )
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='managed_projects',
        verbose_name='Менеджер проекта',
        blank=True,
        null=True
    )
    executor = models.ForeignKey(  # Исполнитель проекта (можно назначить в проекте)
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='assigned_projects',
        verbose_name='Исполнитель проекта',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Модель задачи, связанная с проектом и исполнителем.
    """
    PRIORITY_CHOICES = [
        ('high', 'Высокий'),
        ('medium', 'Средний'),
        ('low', 'Низкий'),
    ]

    STATUS_CHOICES = [
        ('not_started', 'Не начата'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Проект'
    )
    executor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='tasks',
        verbose_name='Исполнитель',
        blank=True,
        null=True
    )
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium',
        verbose_name='Приоритет'
    )
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='not_started',
        verbose_name='Статус'
    )
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.project.name})"


class Comment(models.Model):
    """
    Модель комментария, связанного с задачей.
    """
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Задача'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор'
    )
    content = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Комментарий от {self.author.username} к задаче {self.task.name}"

