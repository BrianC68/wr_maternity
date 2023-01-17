# Generated by Django 3.2.13 on 2023-01-10 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MakingMarriageWorkClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Gottman Seven Principles Program', max_length=200)),
                ('class_date', models.DateField(unique=True)),
                ('start_time', models.TimeField(default=datetime.time(9, 0))),
                ('end_time', models.TimeField(default=datetime.time(17, 30))),
                ('price', models.IntegerField(default=300)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
            options={
                'ordering': ['-class_date'],
            },
        ),
    ]