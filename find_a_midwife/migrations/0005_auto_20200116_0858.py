# Generated by Django 2.2.1 on 2020-01-16 14:58

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_midwife', '0004_auto_20200111_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midwife',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
    ]
