# Generated by Django 3.0.3 on 2020-03-14 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20190830_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester',
            old_name='zoom_room_id',
            new_name='zoom_room_url',
        ),
    ]