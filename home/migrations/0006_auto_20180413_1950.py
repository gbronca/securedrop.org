# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-13 19:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180413_1644'),
        ('directory', '0010_auto_20180413_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepageinstances',
            name='instance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='directory.DirectoryEntry'),
        ),
    ]
