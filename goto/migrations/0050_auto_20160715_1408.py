# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0049_auto_20160715_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gotouser',
            name='profile_picture',
            field=models.ImageField(default='no-photo.jpg', upload_to='profile_pictures/'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(default='no-photo.jpg', upload_to='partners'),
        ),
    ]