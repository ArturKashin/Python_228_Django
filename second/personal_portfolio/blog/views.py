from django.shortcuts import render, get_object_or_404
# импортируем из models.py класс Blog - базу данных
from .models import Blog


def blogs(request):
    # из Models.py/Blog получить все данные
    # blogs = Blog.objects.all()

    # из Models.py/Blog получить все данные с сортировкой по убыванию
    blogs = Blog.objects.order_by('-date')

    # для использования базы на странице, отправляем в виде списка
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    # взять из базы Blog по ключу blog_id или вернуть 404
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/details.html', {'blog': blog})
