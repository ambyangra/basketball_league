# Generated by Django 5.0.6 on 2024-07-07 08:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="team_size",
            field=models.PositiveIntegerField(default=10, verbose_name="Team Size"),
        ),
    ]
