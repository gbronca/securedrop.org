# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-07 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20171103_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footersettings',
            name='donation_link',
            field=models.URLField(default='https://freedom.press/crowdfunding/securedrop/'),
            preserve_default=False,
        ),
    ]