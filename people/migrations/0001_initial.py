# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 00:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('github', models.CharField(blank=True, max_length=40)),
                ('twitter', models.CharField(blank=True, max_length=16)),
                ('web', models.URLField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
