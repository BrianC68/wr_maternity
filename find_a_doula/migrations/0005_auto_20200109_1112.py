# Generated by Django 2.2.1 on 2020-01-09 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_doula', '0004_auto_20200104_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doula',
            name='website_text',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='doula',
            name='website_type',
            field=models.CharField(blank=True, choices=[('WEB', 'Website'), ('PROF', 'Profile'), ('FB', 'Facebook')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='doula',
            name='website_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]