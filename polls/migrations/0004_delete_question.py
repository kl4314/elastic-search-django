# Generated by Django 2.0.1 on 2018-01-09 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180108_2204'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
