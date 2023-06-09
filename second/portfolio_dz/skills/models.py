from django.db import models


class Skills(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='skills/image/')
    url = models.URLField(blank=True)
