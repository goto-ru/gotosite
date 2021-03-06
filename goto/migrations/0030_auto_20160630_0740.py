# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 07:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0029_auto_20160629_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ['-date_created']},
        ),
        migrations.AddField(
            model_name='participant',
            name='parent_phone_number',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='participant',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=40),
            preserve_default=False,
        ),
    ]
