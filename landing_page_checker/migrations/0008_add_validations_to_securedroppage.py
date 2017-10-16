# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 15:12
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page_checker', '0007_securedroppage_search_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='securedroppage',
            name='landing_page_domain',
            field=models.URLField(max_length=255, unique=True, verbose_name='Landing Page Domain Name'),
        ),
        migrations.AlterField(
            model_name='securedroppage',
            name='onion_address',
            field=models.URLField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(regex='\\.onion$')], verbose_name='SecureDrop Onion Address'),
        ),
        migrations.AlterField(
            model_name='securedroppage',
            name='organization_description',
            field=models.CharField(blank=True, help_text='A micro description of your organization that will be displayed in the directory.', max_length=95, null=True),
        ),
        migrations.AlterField(
            model_name='securedroppage',
            name='organization_logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='common.CustomImage', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpc', 'mic', 'ppm', 'png', 'tif', 'ps', 'iim', 'gif', 'sgi', 'dcx', 'psd', 'j2k', 'pgm', 'tga', 'jpe', 'fpx', 'pbm', 'bufr', 'mpeg', 'pcx', 'ras', 'hdf', 'xbm', 'jpeg', 'palm', 'im', 'pcd', 'eps', 'msp', 'grib', 'pxr', 'jp2', 'mpo', 'fit', 'pdf', 'cur', 'gbr', 'wmf', 'ftc', 'j2c', 'bmp', 'emf', 'fits', 'jpx', 'tiff', 'fli', 'rgba', 'jpf', 'bw', 'webp', 'h5', 'jpg', 'dds', 'icns', 'xpm', 'ftu', 'mpg', 'ico', 'rgb', 'flc', 'jfif'])]),
        ),
    ]
