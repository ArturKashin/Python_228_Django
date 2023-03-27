from django.db import models


# создание базы данных
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    # просмотр название статьи в админке, для удобства
    def __str__(self):
        return self.title
