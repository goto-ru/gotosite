# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 21:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0050_auto_20160715_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='format',
            field=models.CharField(blank=True, choices=[('school', 'Школа'), ('hackathon', 'Хакатон'), ('lecture', 'Лекция'), ('other', 'Другое')], max_length=400),
        ),
        migrations.AlterField(
            model_name='project',
            name='event',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='goto.Event'),
        ),
        migrations.AlterField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='goto.Expert'),
        ),
    ]