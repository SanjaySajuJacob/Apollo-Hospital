# Generated by Django 3.2 on 2021-06-22 19:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('apollo', '0011_auto_20210620_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 22, 19, 14, 42, 498346, tzinfo=utc), verbose_name='Last Login'),
        ),
    ]
