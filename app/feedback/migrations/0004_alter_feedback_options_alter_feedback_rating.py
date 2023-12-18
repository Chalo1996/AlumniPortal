# Generated by Django 4.2.4 on 2023-08-28 12:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feedback", "0003_remove_feedback_title_feedback_rating"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="feedback",
            options={
                "verbose_name": "Feedback",
                "verbose_name_plural": "Feedback",
            },
        ),
        migrations.AlterField(
            model_name="feedback",
            name="rating",
            field=models.PositiveIntegerField(
                blank=True, default=None, null=True
            ),
        ),
    ]
