# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-05 15:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page_checker', '0005_securedroppage_organization_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='securedroppage',
            name='organization',
        ),
    ]