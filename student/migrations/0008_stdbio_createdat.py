# Generated by Django 4.1.5 on 2023-02-24 09:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_remove_stdbio_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='stdbio',
            name='createdAt',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
