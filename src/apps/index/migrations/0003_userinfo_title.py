# Generated by Django 3.0.5 on 2020-04-23 17:23

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0002_auto_20200417_1841"),
    ]

    operations = [
        migrations.AddField(
            model_name="userinfo",
            name="title",
            field=models.TextField(blank=True, null=True),
        ),
    ]
