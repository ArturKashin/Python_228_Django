from django.shortcuts import render
# импортируем из models.py класс Skills - базу данных
from .models import Skills


def index(request):
    #  из Models.py/Skills получить все данный
    projects = Skills.objects.all()
    # для использования базы на странице, отправляем в виде списка
    return render(request, 'skills/index.html', {'projects': projects})
