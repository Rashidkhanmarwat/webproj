# Generated by Django 4.1.5 on 2023-02-24 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_stdbio_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stdbio',
            name='date',
        ),
    ]