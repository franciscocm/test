# Generated by Django 3.1 on 2020-09-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientManager', '0003_backlog_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='backlog',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]
