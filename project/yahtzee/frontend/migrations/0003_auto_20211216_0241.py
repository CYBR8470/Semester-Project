# Generated by Django 3.2.10 on 2021-12-16 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_hand_d1_alter_hand_d3_alter_hand_d5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hand',
            name='d1',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='hand',
            name='d2',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='hand',
            name='d3',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='hand',
            name='d5',
            field=models.IntegerField(default=3),
        ),
    ]
