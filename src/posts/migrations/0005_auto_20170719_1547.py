# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-19 14:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20170719_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmerprofile',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
