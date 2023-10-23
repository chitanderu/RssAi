# Generated by Django 3.2.18 on 2023-03-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_reader', '0005_feedtag_feedinfo_sourcename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedurl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='FeedTag',
        ),
    ]
