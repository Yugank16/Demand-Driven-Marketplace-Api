# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-05 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20190305_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='months_old',
            field=models.PositiveSmallIntegerField(),
        ),
    ]