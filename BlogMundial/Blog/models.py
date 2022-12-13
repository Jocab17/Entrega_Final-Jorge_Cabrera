from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.ImageField(null=True, blank=True, upload_to='images/')
    #cuerpo = models.TextField()
    cuerpo = RichTextField(null=True, blank=True)
    fecha = models.DateTimeField(default=datetime.now())
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'pk': self.pk})

class Comentario(models.Model):
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return '%s - %s' % (self.post.titulo, self.nombre)

    def get_absolute_url(self):
        return reverse('post_details', kwargs={'pk': self.post.pk})