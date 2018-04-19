# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-19 16:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0017_rename_taxonomies_models'),
    ]

    operations = [
        migrations.RenameField(
            model_name='directoryentry',
            old_name='temporary_countries',
            new_name='countries',
        ),
        migrations.RenameField(
            model_name='directoryentry',
            old_name='temporary_languages',
            new_name='languages',
        ),
        migrations.RenameField(
            model_name='directoryentry',
            old_name='temporary_topics',
            new_name='topics',
        ),
    ]
