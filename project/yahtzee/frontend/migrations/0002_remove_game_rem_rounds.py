# Generated by Django 4.0 on 2021-12-12 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='rem_rounds',
        ),
    ]
