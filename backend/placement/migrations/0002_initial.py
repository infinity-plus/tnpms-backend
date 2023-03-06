# Generated by Django 4.1.2 on 2023-03-06 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("company", "0001_initial"),
        ("user", "0001_initial"),
        ("placement", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentopening",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user.student"
            ),
        ),
        migrations.AddField(
            model_name="oncampusplaceddetail",
            name="offer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="company.currentopening"
            ),
        ),
        migrations.AddField(
            model_name="oncampusplaceddetail",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user.student"
            ),
        ),
        migrations.AddField(
            model_name="offcampusplaceddetail",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="user.student"
            ),
        ),
    ]
