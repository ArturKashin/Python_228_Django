# импорт путей
from django.urls import path
from . import views

# имя приложения, используется когда большое приложение
app_name = 'blog'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    # просмотр полностью статьи
    path('<int:blog_id>/', views.detail, name='detail')
]