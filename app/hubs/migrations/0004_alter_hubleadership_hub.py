# Generated by Django 4.2.4 on 2023-08-27 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("hubs", "0003_hubleadership"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hubleadership",
            name="hub",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="hub_leaders",
                to="hubs.hub",
            ),
        ),
    ]
