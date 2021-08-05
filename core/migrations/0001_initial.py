# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-05 23:15
from __future__ import unicode_literals

import positions.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Handout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="The display name for the handout, like 'Weird Geo'", max_length=255)),
                ('code', models.CharField(help_text="The version code for the handout, like 'ZGX'", max_length=255)),
                ('prob_url', models.CharField(help_text='The URL for the problems handout', max_length=255)),
                ('soln_url', models.CharField(help_text='The URL for the solutions handout', max_length=255)),
                ('position', positions.fields.PositionField(default=-1, help_text='The ordering of the relative handouts to each other.')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Text description such as 'Fall 2017'", max_length=255, unique=True)),
                ('active', models.BooleanField(default=False, help_text='Whether the semester is currently active (there should thus be at most one active semester)')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='handout',
            unique_together=set([('name', 'code')]),
        ),
    ]
