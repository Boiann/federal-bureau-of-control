# Generated by Django 3.2.18 on 2023-06-29 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbd_app', '0003_event_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
