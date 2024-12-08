from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок задачи")
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['is_completed', 'id']  # Сортировка: сначала невыполненные

