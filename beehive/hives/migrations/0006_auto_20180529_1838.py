# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hives', '0005_auto_20180529_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hivedatamodel',
            name='motherBee',
            field=models.BooleanField(default=False),
        ),
    ]
