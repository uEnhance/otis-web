# Generated by Django 3.2.7 on 2021-09-26 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_auto_20210926_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='last_announce_dismiss',
            new_name='last_email_dismiss',
        ),
    ]
