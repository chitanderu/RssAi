# Generated by Django 4.0.4 on 2023-02-28 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=255)),
                ('img_src', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pub_date', models.TextField()),
            ],
        ),
    ]
