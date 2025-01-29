from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Project, Task, Comment


class CustomUserCreationForm(UserCreationForm):
    """
    Форма регистрации пользователя с выбором роли.
    """
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,  # Предполагается, что в модели есть ROLE_CHOICES
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Роль"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class ProjectForm(forms.ModelForm):
    """
    Форма для создания и редактирования проектов.
    """

    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'status', 'manager',
                  'executor']  # Добавьте 'executor'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название проекта'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Описание проекта'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'manager': forms.Select(attrs={'class': 'form-select'}),
            'executor': forms.Select(attrs={'class': 'form-select'}),  # Поле для выбора исполнителя
        }


class TaskForm(forms.ModelForm):
    """
    Форма для создания и редактирования задач.
    """
    class Meta:
        model = Task
        fields = ['name', 'description', 'project', 'priority', 'status', 'executor', 'start_date', 'end_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название задачи'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Описание задачи'}),
            'project': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'executor': forms.Select(attrs={'class': 'form-select'}),  # поле для выбора исполнителя
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class CommentForm(forms.ModelForm):
    """
    Форма для добавления комментариев к задачам.
    """
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Введите комментарий'}),
        }
        labels = {
            'content': 'Комментарий',
        }
