# Generated by Django 5.0 on 2024-03-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]