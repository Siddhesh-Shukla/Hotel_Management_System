# Generated by Django 3.2 on 2021-04-09 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20210409_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='checkin_time',
            field=models.TimeField(default='09:30:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='checkout_time',
            field=models.TimeField(default='09:30:00'),
            preserve_default=False,
        ),
    ]
