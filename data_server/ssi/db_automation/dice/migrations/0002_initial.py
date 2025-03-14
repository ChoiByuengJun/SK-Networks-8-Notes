# Generated by Django 5.1.3 on 2024-12-04 00:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("dice", "0001_initial"),
        ("game", "0001_initial"),
        ("player", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="dice",
            name="game",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dice",
                to="game.game",
            ),
        ),
        migrations.AddField(
            model_name="dice",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dice",
                to="player.player",
            ),
        ),
    ]
