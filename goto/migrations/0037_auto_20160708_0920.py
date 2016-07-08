# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-08 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0036_auto_20160708_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='date_posted',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solution',
            name='date_verified',
            field=models.DateTimeField(blank=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solution',
            name='participant_comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='solution',
            name='expert',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='goto.Expert'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='expert_comment',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='solution',
            name='file',
            field=models.FileField(blank=True, upload_to='solutions/'),
        ),
    ]
