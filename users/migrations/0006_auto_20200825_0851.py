# Generated by Django 2.2.15 on 2020-08-25 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_remove_user_new_title"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="df",
            new_name="dftest",
        ),
    ]
