# Generated by Django 4.0 on 2021-12-12 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_remove_hand_roll_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='hand',
            name='roll_count',
            field=models.IntegerField(default=3),
        ),
    ]