# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-22 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HiveDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstFrame', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('secondFrame', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('thirdFrame', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('motherBee', models.BooleanField(default=False)),
                ('hive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hives.HiveModel')),
            ],
        ),
    ]
