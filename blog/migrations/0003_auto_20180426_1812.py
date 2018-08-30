# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-26 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180423_1812'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='blogpage',
            index=models.Index(fields=['publication_datetime'], name='blog_blogpa_publica_c7a740_idx'),
        ),
        migrations.AddIndex(
            model_name='blogpage',
            index=models.Index(fields=['category'], name='blog_blogpa_categor_59236c_idx'),
        ),
    ]