# Generated by Django 4.1.3 on 2022-12-08 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_post_fecha_alter_post_subtitulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
