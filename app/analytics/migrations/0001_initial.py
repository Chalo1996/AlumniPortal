# Generated by Django 4.2.3 on 2023-08-10 21:38

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Analytics",
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
            ],
            options={
                "verbose_name": "Analytics",
                "verbose_name_plural": "Analytics",
            },
        ),
    ]
