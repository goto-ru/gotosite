# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-13 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0067_auto_20160813_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gotouser',
            name='sex',
        ),
        migrations.AddField(
            model_name='gotouser',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский'), ('N', 'Не указан')], default='N', max_length=2),
        ),
        migrations.AlterField(
            model_name='participant',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='citizenship',
            field=models.CharField(blank=True, default='Россия', max_length=40),
        ),
        migrations.AlterField(
            model_name='participant',
            name='graduation_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
