# Generated by Django 3.2 on 2021-04-09 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20210409_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='checkin_time',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='checkout_time',
        ),
    ]