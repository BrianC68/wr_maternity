# Generated by Django 2.2.1 on 2020-01-23 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childbirth_classes', '0006_childbirthclassbooking_partner_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childbirthclass',
            name='start_time',
            field=models.TimeField(default=datetime.time(18, 30)),
        ),
    ]
