# Generated by Django 2.2.15 on 2020-09-03 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_remove_user_rating"),
        ("home", "0006_delete_demo"),
    ]

    operations = [
        migrations.DeleteModel(
            name="NewAPP",
        ),
    ]
