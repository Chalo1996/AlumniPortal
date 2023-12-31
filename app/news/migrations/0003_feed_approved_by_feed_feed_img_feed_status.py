# Generated by Django 4.2.4 on 2023-08-16 11:19

import django.db.models.deletion
from django.conf import settings
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("news", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="feed",
            name="approved_by",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="approved_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="feed",
            name="feed_img",
            field=models.ImageField(
                blank=True, null=True, upload_to="feed_img"
            ),
        ),
        migrations.AddField(
            model_name="feed",
            name="status",
            field=models.BooleanField(
                choices=[(True, "Approved"), (False, "Pending")], default=False
            ),
        ),
    ]
