from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    ExecutorTaskStatusUpdateView,
    TaskListView,
    CommentCreateView,
    CustomUserRegisterView,
)

urlpatterns = [
    # ---------------- Проекты ----------------
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

    # ---------------- Задачи ----------------
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/new/', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/update_status/', ExecutorTaskStatusUpdateView.as_view(), name='task_update_status'),  # Обновление статуса задач

    path('task/<int:task_id>/comment/', CommentCreateView.as_view(), name='add_comment'),  # Добавление комментариев
    path('tasks/', TaskListView.as_view(), name='task_list'),

    # ---------------- Аутентификация ----------------
    path('register/', CustomUserRegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='projects/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout')
,
]
