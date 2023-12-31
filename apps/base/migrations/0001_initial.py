# Generated by Django 4.2.3 on 2023-09-08 15:24
from typing import List

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies: List[str] = []

    operations = [
        migrations.CreateModel(
            name="ToDoList",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("task", models.CharField(max_length=150)),
                ("is_done", models.BooleanField(default=False)),
            ],
        ),
    ]
