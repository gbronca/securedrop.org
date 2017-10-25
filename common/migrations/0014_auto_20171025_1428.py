# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('common', '0013_auto_20171017_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='search_image',
        ),
        migrations.DeleteModel(
            name='PersonPage',
        ),
    ]
