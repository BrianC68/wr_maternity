# Generated by Django 3.2.13 on 2023-01-10 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BringingBabyHomeClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Gottman Bringing Baby Home Program', max_length=200)),
                ('class_type', models.CharField(choices=[('8 Week', 'Bringing Baby Home'), ('4 Week', 'Surviving to Thriving')], max_length=25)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField(default=datetime.time(19, 30))),
                ('end_time', models.TimeField(default=datetime.time(21, 0))),
                ('price', models.IntegerField(default=250)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Bringing Baby Home Class',
                'ordering': ['-start_date'],
                'unique_together': {('start_date', 'end_date')},
            },
        ),
    ]
