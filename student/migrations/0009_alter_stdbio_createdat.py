# Generated by Django 4.1.5 on 2023-02-24 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_stdbio_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stdbio',
            name='createdAt',
            field=models.DateTimeField(auto_created=True, blank=True),
        ),
    ]