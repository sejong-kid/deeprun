# Generated by Django 4.1.5 on 2023-02-03 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app", "0005_delete_article_delete_contentinversetable_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=1000, null=True)),
                ("content", models.TextField(null=True)),
                ("date", models.CharField(max_length=20)),
                ("writer", models.CharField(max_length=200)),
                ("href", models.CharField(max_length=1000, null=True)),
                ("title_noun", models.CharField(max_length=5000, null=True)),
                ("content_noun", models.TextField(null=True)),
                ("채용", models.IntegerField(null=True)),
                ("합격자", models.IntegerField(null=True)),
                ("의회", models.IntegerField(null=True)),
                ("행사", models.IntegerField(null=True)),
                ("관람", models.IntegerField(null=True)),
                ("대회", models.IntegerField(null=True)),
                ("의견수렴", models.IntegerField(null=True)),
                ("업체", models.IntegerField(null=True)),
                ("전체교육", models.IntegerField(null=True)),
                ("전문교육", models.IntegerField(null=True)),
                ("청소년", models.IntegerField(null=True)),
                ("주민자치", models.IntegerField(null=True)),
            ],
        ),
    ]