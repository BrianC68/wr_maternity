# Generated by Django 2.2.1 on 2019-12-28 21:36

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0002_auto_20191222_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildbirthClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Well-Rounded Childbirth Class', max_length=200)),
                ('class_type', models.CharField(choices=[('COMP', 'Comprehensive'), ('COND', 'Condensed')], max_length=25)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('price', models.IntegerField(default=275)),
                ('is_active', models.BooleanField(default=True)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cb_location', to='locations.Location')),
            ],
            options={
                'ordering': ['-start_date'],
                'unique_together': {('start_date', 'end_date')},
            },
        ),
        migrations.CreateModel(
            name='ChildbirthClassBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('postal_code', models.CharField(max_length=5)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('paid', models.IntegerField(blank=True, null=True)),
                ('cb_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cb_booking', to='childbirth_classes.ChildbirthClass')),
            ],
            options={
                'ordering': ['last_name'],
                'unique_together': {('first_name', 'last_name', 'email', 'cb_class')},
            },
        ),
    ]