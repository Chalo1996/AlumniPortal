# Generated by Django 4.2.4 on 2023-08-27 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chapters", "0006_merge_20230827_1716"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChapterLeadership",
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
                ("role", models.CharField(max_length=100)),
                (
                    "chapter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chapters.chapter",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Leaders",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Chapter Leadership",
                "unique_together": {("chapter", "user")},
            },
        ),
    ]
