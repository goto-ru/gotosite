# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 07:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0015_auto_20160628_0742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event',
            new_name='question',
        ),
    ]
