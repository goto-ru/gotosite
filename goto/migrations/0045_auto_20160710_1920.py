# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-10 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0044_auto_20160710_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='event',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='goto.Event'),
        ),
    ]
