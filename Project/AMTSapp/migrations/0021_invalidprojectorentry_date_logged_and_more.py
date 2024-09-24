# Generated by Django 5.0.7 on 2024-09-23 09:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMTSapp', '0020_invalidprojectorentry_scrappedprojectorasset'),
    ]

    operations = [
        migrations.AddField(
            model_name='invalidprojectorentry',
            name='date_logged',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='scrappedprojectorasset',
            name='date_logged',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
