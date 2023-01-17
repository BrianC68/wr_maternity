# Generated by Django 3.2.13 on 2023-01-10 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_reminders', '0002_auto_20200117_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminderemail',
            name='email_type',
            field=models.CharField(choices=[('DOULA', 'Doula Workshop'), ('CBCLASS', 'Childbirth Class'), ('BBHCLASS', 'Bringing Baby Home'), ('MMWCLASS', 'Making Marriage Work')], max_length=25, unique=True),
        ),
    ]