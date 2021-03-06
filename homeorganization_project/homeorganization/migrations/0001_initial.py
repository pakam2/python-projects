# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-27 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_of_money', models.DecimalField(decimal_places=2, max_digits=6)),
                ('type_of_expense', models.CharField(max_length=64)),
                ('month_of_expense', models.IntegerField()),
                ('year_of_expense', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_of_money', models.DecimalField(decimal_places=2, max_digits=6)),
                ('type_of_income', models.CharField(max_length=64)),
                ('month_of_income', models.IntegerField()),
                ('year_of_income', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RepeatableExpenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_of_money', models.DecimalField(decimal_places=2, max_digits=6)),
                ('type_of_expense', models.CharField(max_length=64)),
                ('month_of_expense', models.IntegerField()),
                ('year_of_expense', models.IntegerField()),
            ],
        ),
    ]
