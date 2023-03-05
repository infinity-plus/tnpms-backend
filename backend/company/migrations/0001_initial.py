# Generated by Django 4.1.2 on 2023-03-05 18:45

from django.db import migrations, models
import functools
import user.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("is_approved", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=256)),
                ("email_id", models.EmailField(max_length=254)),
                (
                    "phone_number",
                    models.CharField(
                        max_length=10,
                        validators=[
                            functools.partial(
                                user.validators.number_validator, *(), **{"length": 10}
                            )
                        ],
                    ),
                ),
                ("hr_name", models.CharField(max_length=256)),
                ("address", models.TextField()),
                (
                    "company_relation",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Parent"), (2, "Child")]
                    ),
                ),
                ("parent_company_name", models.CharField(max_length=256, null=True)),
                ("industry_type", models.CharField(max_length=256)),
                ("current_employees", models.PositiveBigIntegerField()),
                ("company_type", models.CharField(max_length=256)),
            ],
            options={
                "verbose_name": "Company",
                "verbose_name_plural": "Companies",
            },
        ),
        migrations.CreateModel(
            name="CurrentOpening",
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
                ("is_approved", models.BooleanField(default=False)),
                ("job_title", models.CharField(max_length=256)),
                ("opening_year", models.CharField(max_length=256)),
                (
                    "nature_of_job",
                    models.CharField(
                        max_length=15,
                        validators=[
                            functools.partial(
                                user.validators.number_validator, *(), **{"length": 15}
                            )
                        ],
                    ),
                ),
                ("short_description", models.CharField(max_length=256)),
                ("long_description", models.TextField()),
                ("min_qualification", models.PositiveIntegerField()),
                ("specialization", models.CharField(max_length=256)),
                ("special_skill_requirement", models.TextField()),
                ("vacancy_count", models.PositiveIntegerField()),
                ("vacancy_location", models.PositiveIntegerField()),
                ("min_package", models.PositiveBigIntegerField()),
                ("max_package", models.PositiveBigIntegerField()),
                (
                    "gender_preference",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Male"), (2, "Female"), (3, "Any")]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
