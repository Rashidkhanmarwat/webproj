# Generated by Django 4.1.5 on 2023-02-24 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_rename_roll_stdbio_rollno_alter_stdbio_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stdbio',
            old_name='rollno',
            new_name='roll',
        ),
        migrations.AddField(
            model_name='stdbio',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 24, 13, 53, 0, 417897)),
        ),
    ]
