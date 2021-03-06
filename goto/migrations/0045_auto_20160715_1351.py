# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0044_auto_20160715_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='about_us_command',
            field=models.ManyToManyField(blank=True, to='goto.Expert'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='about_us_partners',
            field=models.ManyToManyField(blank=True, related_name='about_us_partners', to='goto.Partner'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='index_partners',
            field=models.ManyToManyField(blank=True, related_name='index_partners', to='goto.Partner'),
        ),
    ]
