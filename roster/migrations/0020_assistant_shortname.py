# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-25 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0019_auto_20180825_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='assistant',
            name='shortname',
            field=models.CharField(default='??', help_text='Initials or short name for this Assistant', max_length=10),
            preserve_default=False,
        ),
    ]