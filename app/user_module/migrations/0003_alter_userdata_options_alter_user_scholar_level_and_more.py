# Generated by Django 4.2.4 on 2023-08-11 08:10

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ("user_module", "0002_alter_userdata_scholar_code_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userdata",
            options={
                "verbose_name": "Scholar Verification Data",
                "verbose_name_plural": "Scholar Verification Data",
            },
        ),
        migrations.AlterField(
            model_name="user",
            name="scholar_level",
            field=models.CharField(
                blank=True,
                choices=[
                    ("TVET", "TVET"),
                    ("College", "College"),
                    ("University", "University"),
                    ("Alumni", "Alumni"),
                ],
                max_length=30,
                null=True,
                verbose_name="Scholar Education Level",
            ),
        ),
        migrations.AlterField(
            model_name="userdata",
            name="PF",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
