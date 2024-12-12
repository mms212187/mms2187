from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно! Вы можете войти в систему.')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации. Пожалуйста, проверьте данные.')
    else:
        form = UserRegisterForm()
    return render(request, 'learn_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('profile')
        else:
            messages.error(request, 'Ошибка входа. Проверьте имя пользователя и пароль.')
    else:
        form = AuthenticationForm()
    return render(request, 'learn_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Вы успешно вышли из системы.')
    return redirect('login')

@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлён!')
            return redirect('profile')
        else:
            messages.error(request, 'Ошибка обновления профиля. Пожалуйста, проверьте введённые данные.')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'learn_app/profile.html', {'form': form})
