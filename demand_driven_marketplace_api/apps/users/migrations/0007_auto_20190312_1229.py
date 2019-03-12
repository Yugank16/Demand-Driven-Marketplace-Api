# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-12 12:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190312_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must contain 10 digits.', regex='^[6-9]{1}\\d{9}$')]),
        ),
    ]
