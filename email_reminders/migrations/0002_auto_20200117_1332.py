# Generated by Django 2.2.1 on 2020-01-17 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_reminders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminderemail',
            name='email_type',
            field=models.CharField(choices=[('DOULA', 'Doula Workshop'), ('CBCLASS', 'Childbirth Class')], max_length=25, unique=True),
        ),
    ]