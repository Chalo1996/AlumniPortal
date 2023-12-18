# Generated by Django 4.2.4 on 2023-08-22 08:22

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        (
            "user_module",
            "0019_remove_user_scholar_level_profileinfo_scholar_level",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="profileinfo",
            name="employment_status",
            field=models.CharField(
                blank=True,
                max_length=200,
                null=True,
                verbose_name="Current Employment Status",
            ),
        ),
    ]
