# Generated by Django 4.2.3 on 2023-08-10 21:38

import django.db.models.deletion
from django.conf import settings
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("news", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="feed",
            name="posted_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
