# Generated by Django 3.2.13 on 2023-01-10 17:38

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('bringing_baby_home', '0002_auto_20230110_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='BringingBabyHomeClassBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('partner_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('postal_code', models.CharField(max_length=5)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('paid', models.IntegerField(blank=True, null=True)),
                ('bbh_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bbh_booking', to='bringing_baby_home.bringingbabyhomeclass')),
            ],
            options={
                'ordering': ['last_name'],
                'unique_together': {('first_name', 'last_name', 'email', 'bbh_class')},
            },
        ),
    ]
