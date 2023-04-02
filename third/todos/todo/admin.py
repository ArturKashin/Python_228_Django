from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    # набор полей только для чтения
    readonly_fields = ('created',)


admin.site.register(Todo, TodoAdmin)
