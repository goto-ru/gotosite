# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-01 08:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0064_auto_20160801_0730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='event',
            new_name='arrangement',
        ),
    ]