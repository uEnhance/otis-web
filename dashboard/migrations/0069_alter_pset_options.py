# Generated by Django 3.2.9 on 2021-12-01 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0068_alter_achievement_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pset',
            options={
                'verbose_name': 'PSet submission',
                'verbose_name_plural': 'PSet submissions'
            },
        ),
    ]
