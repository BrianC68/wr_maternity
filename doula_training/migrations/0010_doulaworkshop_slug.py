# Generated by Django 2.2.1 on 2020-01-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doula_training', '0009_auto_20191228_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='doulaworkshop',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
