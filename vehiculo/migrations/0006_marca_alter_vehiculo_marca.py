# Generated by Django 5.1.1 on 2024-09-30 15:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vehiculo", "0005_alter_vehiculo_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Marca",
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
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="vehiculo",
            name="marca",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="vehiculo.marca"
            ),
        ),
    ]