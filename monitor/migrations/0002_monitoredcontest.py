# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitoredContest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stavpoisk_id', models.IntegerField()),
            ],
        ),
    ]