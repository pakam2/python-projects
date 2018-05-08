# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-04 20:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HiveModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfHive', models.IntegerField()),
                ('firstFrame', models.DecimalField(decimal_places=2, max_digits=3)),
                ('secondFrame', models.DecimalField(decimal_places=2, max_digits=3)),
                ('thirdFrame', models.DecimalField(decimal_places=2, max_digits=3)),
                ('motherBee', models.BooleanField(default=False)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('comments', models.CharField(max_length=500)),
            ],
        ),
    ]