# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 23:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_auto_20161026_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tool',
            old_name='github_url',
            new_name='code_url',
        ),
    ]
