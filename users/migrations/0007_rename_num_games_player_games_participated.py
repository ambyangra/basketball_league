# Generated by Django 5.0.6 on 2024-07-07 11:31

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_alter_player_average_score_alter_player_num_games"),
    ]

    operations = [
        migrations.RenameField(
            model_name="player",
            old_name="num_games",
            new_name="games_participated",
        ),
    ]