# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0028_auto_20160629_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='graduation_year',
            field=models.IntegerField(blank=True, default=2016),
        ),
    ]
