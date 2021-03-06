# Generated by Django 2.0.4 on 2018-05-01 19:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('url', models.URLField(max_length=300)),
                ('img_url', models.URLField(max_length=300)),
                ('content', models.TextField(blank=True, max_length=500)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
