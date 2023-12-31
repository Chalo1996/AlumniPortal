# Generated by Django 4.2.4 on 2023-08-11 08:30

import django.core.validators
from django.db import (
    migrations,
    models,
)

import app.user_module.constant


class Migration(migrations.Migration):
    dependencies = [
        (
            "user_module",
            "0003_alter_userdata_options_alter_user_scholar_level_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="qualificationinfo",
            name="other_skills",
        ),
        migrations.AddField(
            model_name="workexperienceinfo",
            name="description",
            field=models.TextField(
                blank=True, verbose_name="Description / Achievements"
            ),
        ),
        migrations.AlterField(
            model_name="addressinfo",
            name="country",
            field=models.CharField(
                blank=True, max_length=136, verbose_name="Country Of Residence"
            ),
        ),
        migrations.AlterField(
            model_name="addressinfo",
            name="home_county",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="Home County"
            ),
        ),
        migrations.AlterField(
            model_name="addressinfo",
            name="residence_county",
            field=models.CharField(
                blank=True, max_length=50, verbose_name="County of Residence"
            ),
        ),
        migrations.AlterField(
            model_name="educationinfo",
            name="course_cluster",
            field=models.CharField(
                blank=True, max_length=250, verbose_name="Course Cluster"
            ),
        ),
        migrations.AlterField(
            model_name="educationinfo",
            name="graduation_year",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1984),
                    app.user_module.constant.max_value_current_year,
                ],
                verbose_name="Year of Graduation",
            ),
        ),
        migrations.AlterField(
            model_name="educationinfo",
            name="institution_category",
            field=models.CharField(blank=True, max_length=130),
        ),
        migrations.AlterField(
            model_name="educationinfo",
            name="institution_country",
            field=models.CharField(blank=True, max_length=130),
        ),
        migrations.AlterField(
            model_name="educationinfo",
            name="institution_level",
            field=models.CharField(
                blank=True, max_length=230, verbose_name="Institution Level"
            ),
        ),
        migrations.AlterField(
            model_name="educationinfo",
            name="year_of_study",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Year of Study"
            ),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="gender",
            field=models.CharField(
                blank=True, max_length=110, null=True, verbose_name="Gender"
            ),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="home_branch",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="marital_status",
            field=models.CharField(
                blank=True, max_length=250, verbose_name="Marital Status"
            ),
        ),
        migrations.AlterField(
            model_name="personalinfo",
            name="title",
            field=models.CharField(
                blank=True, max_length=55, verbose_name="Title"
            ),
        ),
        migrations.AlterField(
            model_name="qualificationinfo",
            name="employment_status",
            field=models.CharField(
                blank=True,
                max_length=200,
                verbose_name="Current Employment Status",
            ),
        ),
        migrations.AlterField(
            model_name="qualificationinfo",
            name="skills",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Skills"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="scholar_level",
            field=models.CharField(
                blank=True,
                max_length=30,
                null=True,
                verbose_name="Scholar Education Level",
            ),
        ),
        migrations.AlterField(
            model_name="workexperienceinfo",
            name="type_of_business",
            field=models.CharField(
                blank=True, max_length=230, verbose_name="Type of Business"
            ),
        ),
    ]
