# Generated by Django 4.1.2 on 2022-11-08 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Proveedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=128)),
                (
                    "type_proveedor",
                    models.TextField(
                        choices=[
                            ("Hotel", "Hotel"),
                            ("Pista", "Pista"),
                            ("Complemento", "Complemento"),
                        ]
                    ),
                ),
                ("active", models.BooleanField()),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("update_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]