# Generated by Django 4.0.7 on 2022-09-22 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0086_auto_20220805_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='reg',
            field=models.OneToOneField(blank=True, help_text='Link to the registration forms for the student', null=True, on_delete=django.db.models.deletion.SET_NULL, to='roster.studentregistration'),
        ),
    ]