# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-12-06 16:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models

import dashboard.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_uploadedfile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='content',
            field=models.FileField(help_text='The file itself', upload_to=dashboard.models.content_file_name, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'txt', 'tex'])]),
        ),
    ]
