# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-22 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20170719_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendQuotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_product', models.CharField(max_length=200)),
                ('qty_of_product', models.FloatField()),
                ('address', models.CharField(max_length=500)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
