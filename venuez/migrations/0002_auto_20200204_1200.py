# Generated by Django 3.0.3 on 2020-02-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venuez', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='civilID',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='paci_no',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
