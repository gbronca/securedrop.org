# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_directorysettings_no_results_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='personpage',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage'),
        ),
    ]
