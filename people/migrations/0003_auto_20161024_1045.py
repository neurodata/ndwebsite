# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20161012_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AlterModelOptions(
            name='people',
            options={'ordering': ('name',), 'verbose_name_plural': 'people'},
        ),
        migrations.AddField(
            model_name='people',
            name='position',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name='people',
            name='roles',
            field=models.ManyToManyField(to='people.Role'),
        ),
    ]
