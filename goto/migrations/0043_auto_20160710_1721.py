# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-10 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0042_participant__subscribed_to_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='format',
            field=models.CharField(blank=True, choices=[('school', 'Школа'), ('hackathon', 'Хакатон'), ('lecture', 'Лекция')], max_length=400),
        ),
    ]
