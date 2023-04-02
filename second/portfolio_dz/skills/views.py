from django.shortcuts import render, redirect
from .models import Skills
# формы регистрации пользователя; авторизации пользователей
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# импорт модели пользователя(User)
from django.contrib.auth.models import User
# ошибки при работе с базой данных
from django.db import IntegrityError
# автоматическая авторизация при регистрации; выход из аккаунта; аутентификация
from django.contrib.auth import login, logout, authenticate


def index(request):
    projects = Skills.objects.all()
    return render(request, 'skills/index.html', {'projects': projects})


# регистрация пользователя
def signupuser(request):
    if request.method == "GET":
        return render(request, 'skills/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            # запись нового пользователя
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'skills/signupuser.html', {
                    'form': UserCreationForm(),
                    'error': 'Такое имя пользователя уже существует'
                })
        else:
            return render(request, 'skills/signupuser.html', {
                'form': UserCreationForm(),
                'error': 'Пароли не совпадают'
            })


def loginuser(request):
    if request.method == "GET":
        return render(request, 'skills/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'skills/loginuser.html', {
                'form': AuthenticationForm(),
                'error': 'Неверные данные для входа'
            })
        else:
            login(request, user)
            return redirect('index')


def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('index')