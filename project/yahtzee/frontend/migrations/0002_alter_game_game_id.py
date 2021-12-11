# Generated by Django 3.2.10 on 2021-12-10 22:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
