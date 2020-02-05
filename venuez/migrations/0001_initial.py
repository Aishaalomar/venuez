# Generated by Django 3.0.3 on 2020-02-04 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('reservation', models.DateField()),
                ('comments', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('NONE', 'None'), ('OWNER', 'Owner'), ('CUSTOMER', 'Customer')], default='NONE', max_length=8)),
                ('paci_no', models.CharField(max_length=12, null=True)),
                ('civilID', models.CharField(max_length=12, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=130)),
                ('name', models.CharField(max_length=100)),
                ('price_per_day', models.DecimalField(decimal_places=3, max_digits=10)),
                ('description', models.TextField()),
                ('capacity', models.IntegerField()),
                ('availability', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venuez.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Venue_Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venuez.Venue')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField()),
                ('comment', models.TextField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venuez.Booking')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venuez.Profile')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venuez.Venue')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venuez.Profile'),
        ),
        migrations.AddField(
            model_name='booking',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venuez.Venue'),
        ),
    ]