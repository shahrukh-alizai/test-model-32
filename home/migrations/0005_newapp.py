# Generated by Django 2.2.15 on 2020-09-03 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_demo"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewAPP",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("idasd", models.BigIntegerField()),
            ],
        ),
    ]
