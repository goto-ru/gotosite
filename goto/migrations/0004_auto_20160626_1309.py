# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-26 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goto', '0003_auto_20160624_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=10000)),
                ('slug', models.SlugField(max_length=256, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='pages',
            field=models.ManyToManyField(to='goto.Page'),
        ),
    ]