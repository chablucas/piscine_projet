# Generated by Django 4.2.7 on 2023-12-01 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogMovies', '0002_post_poster_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
