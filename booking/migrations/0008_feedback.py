# Generated by Django 3.2 on 2021-04-18 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20210409_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.PositiveSmallIntegerField(choices=[(1, 'Very Satisfied'), (2, 'Satisfied'), (3, 'Unsatisfied')])),
                ('q2', models.PositiveSmallIntegerField(choices=[(1, 'Very Satisfied'), (2, 'Satisfied'), (3, 'Unsatisfied')])),
                ('q3', models.PositiveSmallIntegerField(choices=[(1, 'Very Satisfied'), (2, 'Satisfied'), (3, 'Unsatisfied')])),
                ('q4', models.PositiveSmallIntegerField(choices=[(1, 'Very Satisfied'), (2, 'Satisfied'), (3, 'Unsatisfied')])),
                ('q5', models.PositiveSmallIntegerField(choices=[(1, 'Very Satisfied'), (2, 'Satisfied'), (3, 'Unsatisfied')])),
                ('q6', models.PositiveSmallIntegerField(choices=[(1, 'Very Satisfied'), (2, 'Satisfied'), (3, 'Unsatisfied')])),
                ('q7', models.PositiveSmallIntegerField(choices=[(1, 'Very Satisfied'), (2, 'Satisfied'), (3, 'Unsatisfied')])),
            ],
        ),
    ]
