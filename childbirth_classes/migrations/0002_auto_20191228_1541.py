# Generated by Django 2.2.1 on 2019-12-28 21:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('childbirth_classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childbirthclass',
            name='end_time',
            field=models.TimeField(default=datetime.time(21, 0)),
        ),
        migrations.AlterField(
            model_name='childbirthclass',
            name='location',
            field=models.ForeignKey(default=3, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cb_location', to='locations.Location'),
        ),
        migrations.AlterField(
            model_name='childbirthclass',
            name='start_time',
            field=models.TimeField(default=datetime.time(16, 30)),
        ),
    ]
