# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0048_expert_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expert',
            name='short_description',
            field=models.CharField(blank=True, default='', max_length=256),
            preserve_default=False,
        ),
    ]
