# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-05 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeorganization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.TextField()),
                ('whos_task', models.CharField(max_length=64)),
                ('end_date', models.DateField()),
            ],
        ),
    ]
