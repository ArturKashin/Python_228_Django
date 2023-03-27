from django.contrib import admin
from .models import Skills

# регистрация таблицы из бд в админке
admin.site.register(Skills)
