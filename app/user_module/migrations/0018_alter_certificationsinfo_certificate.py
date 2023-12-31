# Generated by Django 4.2.4 on 2023-08-20 11:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_module", "0017_certificationsinfo_certificate_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="certificationsinfo",
            name="certificate",
            field=cloudinary.models.CloudinaryField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Certificate",
            ),
        ),
    ]
