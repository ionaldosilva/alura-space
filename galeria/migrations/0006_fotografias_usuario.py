# Generated by Django 4.2.3 on 2023-07-27 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("galeria", "0005_alter_fotografias_foto"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografias",
            name="usuario",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
