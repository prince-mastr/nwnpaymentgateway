# Generated by Django 2.2.4 on 2020-08-09 18:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0002_auto_20200809_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='authorization_code',
            field=models.CharField(default='1234567812345678', max_length=20),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='create_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 9, 18, 58, 17, 54506)),
        ),
    ]
