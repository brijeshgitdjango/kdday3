# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-24 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20181024_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='room',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='room.Room'),
        ),
    ]
