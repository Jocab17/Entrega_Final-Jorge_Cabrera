# Generated by Django 4.1.4 on 2022-12-11 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_alter_post_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 11, 12, 16, 32, 761331)),
        ),
    ]
