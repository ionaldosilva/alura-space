# Generated by Django 4.2.3 on 2023-07-24 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografias",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("NEBULOSA", "Nebulosa"),
                    ("GALÁXIA", "Galáxia"),
                    ("ESTRELA", "Estrela"),
                    ("PLANETA", "Planeta"),
                ],
                default="",
                max_length=100,
            ),
        ),
    ]
