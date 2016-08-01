# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-10 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0043_auto_20160710_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='format',
            field=models.CharField(blank=True, choices=[('school', 'Школа'), ('hackathon', 'Хакатон'), ('lecture', 'Лекция'), ('other', 'Лекция')], max_length=400),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(default='Пустой проект', max_length=256),
        ),
    ]
