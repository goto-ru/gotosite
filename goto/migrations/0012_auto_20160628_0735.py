# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0011_auto_20160627_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='pages',
            field=models.ManyToManyField(blank=True, to='goto.Page'),
        ),
    ]