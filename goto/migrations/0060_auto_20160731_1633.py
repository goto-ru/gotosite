# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-31 16:33
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0059_departments_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Image'),
        ),
    ]
