# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-03 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0033_auto_20160701_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantcomment',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='projectcomment',
            name='is_private',
            field=models.BooleanField(default=True),
        ),
    ]
