# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-17 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0051_auto_20160715_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='gotouser',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
