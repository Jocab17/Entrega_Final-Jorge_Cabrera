# Generated by Django 4.1.4 on 2022-12-13 01:32

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0016_alter_comentario_fecha_alter_post_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 22, 32, 55, 34011)),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 12, 22, 32, 55, 18383)),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
