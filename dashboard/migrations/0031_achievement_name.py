# Generated by Django 3.2.5 on 2021-08-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_rename_achievementcode_achievement'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='name',
            field=models.CharField(
                default='', help_text='Name of the achievement', max_length=128),
            preserve_default=False,
        ),
    ]
