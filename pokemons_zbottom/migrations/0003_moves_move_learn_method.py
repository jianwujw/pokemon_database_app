# Generated by Django 4.2.4 on 2023-09-08 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemons_zbottom', '0002_remove_moves_game_version_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moves',
            name='move_learn_method',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pokemons_zbottom.movesmethod'),
        ),
    ]
