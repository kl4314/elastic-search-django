# Generated by Django 2.0.1 on 2018-01-08 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_movie_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_info',
            name='pub_date',
            field=models.CharField(max_length=200),
        ),
    ]