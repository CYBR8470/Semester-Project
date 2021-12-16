# Generated by Django 4.0 on 2021-12-16 02:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_public', models.BooleanField(default=True)),
                ('join_code', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('is_open', models.BooleanField(default=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ones', models.IntegerField(null=True)),
                ('twos', models.IntegerField(null=True)),
                ('threes', models.IntegerField(null=True)),
                ('fours', models.IntegerField(null=True)),
                ('fives', models.IntegerField(null=True)),
                ('sixes', models.IntegerField(null=True)),
                ('three_oak', models.IntegerField(null=True)),
                ('four_oak', models.IntegerField(null=True)),
                ('full_house', models.IntegerField(null=True)),
                ('small_straight', models.IntegerField(null=True)),
                ('large_straight', models.IntegerField(null=True)),
                ('yahtzee', models.IntegerField(null=True)),
                ('chance', models.IntegerField(null=True)),
                ('bonus_yahtzees', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Hand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d1', models.IntegerField(default=5)),
                ('d2', models.IntegerField(default=4)),
                ('d3', models.IntegerField(default=1)),
                ('d4', models.IntegerField(default=3)),
                ('d5', models.IntegerField(default=2)),
                ('roll_count', models.IntegerField(default=2)),
                ('rem_rounds', models.IntegerField(default=13)),
                ('yahtzee_flag', models.IntegerField(null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(related_name='board', to='frontend.Hand'),
        ),
        migrations.AddField(
            model_name='game',
            name='scores',
            field=models.ManyToManyField(related_name='board', to='frontend.Score'),
        ),
    ]
