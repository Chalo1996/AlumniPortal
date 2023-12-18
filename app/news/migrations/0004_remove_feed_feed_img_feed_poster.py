# Generated by Django 4.2.4 on 2023-08-16 11:27

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_feed_approved_by_feed_feed_img_feed_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="feed",
            name="feed_img",
        ),
        migrations.AddField(
            model_name="feed",
            name="poster",
            field=cloudinary.models.CloudinaryField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Feed Poster",
            ),
        ),
    ]
