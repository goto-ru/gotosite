# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-10 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0045_auto_20160710_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goto.Event'),
        ),
    ]