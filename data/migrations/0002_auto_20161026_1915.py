# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_squashed_0007_auto_20161012_0046'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ('name',),
            },
        )
    ]
