# Generated by Django 2.2.15 on 2020-08-25 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20200825_0711"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="title",
            new_name="new_title",
        ),
    ]
