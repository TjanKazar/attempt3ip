# Generated by Django 4.1 on 2024-06-06 16:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("webapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prijavnica",
            name="komentar",
        ),
        migrations.RemoveField(
            model_name="prijavnica",
            name="valid",
        ),
    ]