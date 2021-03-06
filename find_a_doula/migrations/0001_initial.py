# Generated by Django 2.2.1 on 2019-12-31 16:27

import ckeditor.fields
from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoulaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('photo', models.ImageField(upload_to='doulas')),
                ('service_area', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('website_type', models.CharField(max_length=25)),
                ('website_text', models.CharField(max_length=100)),
                ('website_url', models.URLField()),
            ],
            options={
                'ordering': ['name'],
                'unique_together': {('name', 'email', 'phone')},
            },
        ),
    ]
