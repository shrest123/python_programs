# Generated by Django 3.1.6 on 2021-02-27 03:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('trello_app', '0002_auto_20210227_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_list',
            name='created_id',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 27, 3, 34, 32, 73250, tzinfo=utc)),
        ),
    ]