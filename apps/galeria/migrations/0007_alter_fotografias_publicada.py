# Generated by Django 4.2.3 on 2023-07-27 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("galeria", "0006_fotografias_usuario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fotografias",
            name="publicada",
            field=models.BooleanField(default=True),
        ),
    ]