# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 21:05
from __future__ import unicode_literals

from django.db import migrations, models

import dashboard.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20170814_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='category',
            field=models.CharField(choices=[('psets', 'PSet Submission'), ('scripts', 'Transcript'), ('notes', 'Notes / Comments'), ('misc', 'Miscellaneous')], help_text='What kind of file this is', max_length=10),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='content',
            field=models.FileField(help_text='The file itself', upload_to=dashboard.models.content_file_name),
        ),
    ]
