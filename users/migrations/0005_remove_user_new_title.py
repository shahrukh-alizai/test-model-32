# Generated by Django 2.2.15 on 2020-08-25 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_df'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='new_title',
        ),
    ]