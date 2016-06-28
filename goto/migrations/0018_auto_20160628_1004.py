# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 10:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0017_auto_20160628_0745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer',
            new_name='text',
        ),
        migrations.AddField(
            model_name='answer',
            name='event',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='goto.Event'),
            preserve_default=False,
        ),
    ]
