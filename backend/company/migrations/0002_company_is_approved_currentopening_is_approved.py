# Generated by Django 4.1.2 on 2023-02-25 09:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="company",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="currentopening",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
    ]
