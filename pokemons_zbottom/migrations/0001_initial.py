# Generated by Django 4.2.4 on 2023-09-01 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Moves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=30)),
                ('level', models.PositiveIntegerField()),
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('image_url', models.URLField(blank=True)),
                ('abilities', models.ManyToManyField(to='pokemons_zbottom.abilities')),
                ('moves', models.ManyToManyField(to='pokemons_zbottom.moves')),
            ],
        ),
    ]
