# Generated by Django 4.0 on 2021-12-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_game_rem_rounds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]