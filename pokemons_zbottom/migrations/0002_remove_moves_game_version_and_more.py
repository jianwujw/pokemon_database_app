# Generated by Django 4.2.4 on 2023-09-08 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons_zbottom', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moves',
            name='game_version',
        ),
        migrations.RemoveField(
            model_name='moves',
            name='move_learn_method',
        ),
    ]
