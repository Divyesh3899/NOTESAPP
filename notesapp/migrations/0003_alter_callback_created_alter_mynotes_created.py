# Generated by Django 4.2.3 on 2024-01-08 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0002_alter_callback_created_alter_mynotes_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callback',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 8, 17, 24, 53, 361019)),
        ),
        migrations.AlterField(
            model_name='mynotes',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 8, 17, 24, 53, 361019)),
        ),
    ]
