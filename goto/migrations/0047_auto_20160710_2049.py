# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-10 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0046_auto_20160710_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goto.Expert'),
        ),
    ]
