# Generated by Django 4.1.5 on 2023-02-24 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_alter_stdbio_createdat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stdbio',
            name='createdAt',
        ),
    ]
