# Generated by Django 2.1.7 on 2019-10-11 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster', '0028_auto_20191011_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitinquiry',
            name='action_type',
            field=models.CharField(
                choices=[('DROP', 'Drop'), ('JUMP', 'Unlock'), ('ADD', 'Add later')],
                help_text='Describe the action you want to make.',
                max_length=10),
        ),
    ]
