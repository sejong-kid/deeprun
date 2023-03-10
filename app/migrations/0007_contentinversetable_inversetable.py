# Generated by Django 4.1.5 on 2023-02-03 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContentInverseTable",
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
                ("word", models.CharField(max_length=100, null=True)),
                ("frequency", models.IntegerField(null=True)),
                ("location", models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="InverseTable",
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
                ("word", models.CharField(max_length=100, null=True)),
                ("frequency", models.IntegerField(null=True)),
                ("location", models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
