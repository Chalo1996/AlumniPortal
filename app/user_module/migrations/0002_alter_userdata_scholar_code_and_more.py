# Generated by Django 4.2.4 on 2023-08-11 07:43

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ("user_module", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdata",
            name="scholar_code",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="userdata",
            name="scholar_type",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
