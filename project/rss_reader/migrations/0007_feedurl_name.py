# Generated by Django 3.2.18 on 2023-03-15 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_reader', '0006_auto_20230315_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedurl',
            name='name',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
