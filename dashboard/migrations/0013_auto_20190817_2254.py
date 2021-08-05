# Generated by Django 2.1.7 on 2019-08-18 03:54

import django.core.validators
from django.db import migrations, models

import dashboard.models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20190327_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='content',
            field=models.FileField(help_text='The file itself', upload_to=dashboard.models.content_file_name, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'txt', 'tex', 'png', 'jpg'])]),
        ),
    ]
