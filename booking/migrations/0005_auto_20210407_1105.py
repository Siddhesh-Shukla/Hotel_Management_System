# Generated by Django 3.2 on 2021-04-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20210406_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('adults', models.PositiveIntegerField()),
                ('children', models.PositiveIntegerField()),
                ('roomtype', models.TextField(max_length=15)),
                ('rooms', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Bookings',
        ),
    ]