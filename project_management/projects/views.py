from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # Импорт обоих классов
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import CustomUser, Project, Task, Comment
from .forms import ProjectForm, TaskForm, CommentForm, CustomUserCreationForm
from django import forms

# ----------------- Дополнительная форма для изменения статуса задачи исполнителем ----------------- #
class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']  # Разрешаем менять только статус


# ----------------- Представление для регистрации пользователя ----------------- #
class CustomUserRegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'projects/register.html'
    success_url = reverse_lazy('login')  # Перенаправление на страницу входа после регистрации


# ----------------- Список проектов ----------------- #
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    login_url = 'login'  # Если пользователь не авторизован, перенаправлять на страницу логина

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '')
        status = self.request.GET.get('status', '')
        sort_by = self.request.GET.get('sort_by', '')

        user = self.request.user
        # Фильтрация по роли
        if user.is_authenticated and hasattr(user, 'role'):
            if user.role == 'manager':
                # Менеджер видит только проекты, где он указан как manager
                queryset = queryset.filter(manager=user)
            elif user.role == 'executor':
                # Исполнитель видит только проекты, в которых у него есть задачи
                queryset = queryset.filter(tasks__executor=user).distinct()

        # Фильтрация по поиску, статусу, сортировке
        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if status:
            queryset = queryset.filter(status=status)
        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset


# ----------------- Детали проекта ----------------- #
class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'
    login_url = 'login'


# ----------------- Создание проекта (Admin / Manager) ----------------- #
class ProjectCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')
    login_url = 'login'

    def test_func(self):
        """
        Только администратор и менеджер могут создавать проекты.
        """
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'role')
            and self.request.user.role in ['admin', 'manager']
        )

    def form_valid(self, form):
        """
        Если пользователь - manager, автоматически проставляем поле manager у проекта.
        Администратор может выбрать: оставить поле manager пустым в форме или заполнить вручную.
        """
        project = form.save(commit=False)
        user = self.request.user
        if user.is_authenticated and hasattr(user, 'role'):
            if user.role == 'manager':
                project.manager = user
            # Если admin, можно оставить manager=None или заполнить вручную в форме
        project.save()
        return super().form_valid(form)


# ----------------- Редактирование проекта (Admin / Manager) ----------------- #
class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')
    login_url = 'login'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'role')
            and self.request.user.role in ['admin', 'manager']
        )


# ----------------- Удаление проекта (Admin / Manager) ----------------- #
class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')
    login_url = 'login'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'role')
            and self.request.user.role in ['admin', 'manager']
        )


# ----------------- Детали задачи ----------------- #
class TaskDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Task
    template_name = 'projects/task_detail.html'
    context_object_name = 'task'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Форма для добавления комментариев
        context['form'] = CommentForm()
        return context

    def test_func(self):
        """
        Исполнитель может видеть только свои задачи.
        Админ / Менеджер могут видеть любые задачи.
        """
        task = self.get_object()
        user = self.request.user
        if user.is_authenticated and hasattr(user, 'role'):
            if user.role == 'executor':
                return (task.executor == user)
            return user.role in ['admin', 'manager']
        return False


# ----------------- Создание / Редактирование задачи (Admin / Manager) ----------------- #
class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'projects/task_form.html'
    success_url = reverse_lazy('project_list')
    login_url = 'login'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'role')
            and self.request.user.role in ['admin', 'manager']
        )


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'projects/task_form.html'
    success_url = reverse_lazy('project_list')
    login_url = 'login'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'role')
            and self.request.user.role in ['admin', 'manager']
        )


# ----------------- Удаление задачи (Admin / Manager) ----------------- #
class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'projects/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
    login_url = 'login'

    def test_func(self):
        return (
            self.request.user.is_authenticated
            and hasattr(self.request.user, 'role')
            and self.request.user.role in ['admin', 'manager']
        )


# ----------------- Список задач ----------------- #
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'projects/task_list.html'
    context_object_name = 'tasks'
    login_url = 'login'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '')
        priority = self.request.GET.get('priority', '')
        sort_by = self.request.GET.get('sort_by', '')

        user = self.request.user
        if user.is_authenticated and hasattr(user, 'role'):
            if user.role == 'executor':
                # Исполнитель видит только свои задачи
                queryset = queryset.filter(executor=user)
            elif user.role == 'manager':
                # Менеджер видит задачи в проектах, где он manager
                queryset = queryset.filter(project__manager=user)

        if query:
            queryset = queryset.filter(Q(name__icontains=query) | Q(description__icontains=query))
        if priority:
            queryset = queryset.filter(priority=priority)
        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset


# ----------------- Обновление только статуса задачи исполнителем ----------------- #
class ExecutorTaskStatusUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    template_name = 'projects/task_status_update.html'
    success_url = reverse_lazy('task_list')
    login_url = 'login'

    class StatusForm(forms.ModelForm):
        class Meta:
            model = Task
            fields = ['status']

    form_class = StatusForm

    def test_func(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, 'role') and user.role == 'executor':
            task = self.get_object()
            return (task.executor == user)
        return False


# ----------------- Добавление комментария ----------------- #
class CommentCreateView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user  # Устанавливаем автора комментария как текущего пользователя
            comment.save()
        return redirect('task_detail', pk=task_id)
