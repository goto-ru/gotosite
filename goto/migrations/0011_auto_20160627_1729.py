# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0010_auto_20160627_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='goto.Event'),
        ),
    ]
