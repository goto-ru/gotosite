# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-13 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0066_auto_20160801_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='current_hackathon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='settings_3', to='goto.Event'),
        ),
    ]