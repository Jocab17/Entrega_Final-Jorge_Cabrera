from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(default=datetime.now())
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('post_details', args=(str(self.id)))