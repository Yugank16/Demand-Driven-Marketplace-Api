# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-05 07:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20190305_0730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('short_desc', models.CharField(max_length=512)),
                ('date_time', models.DateTimeField()),
                ('item_state', models.PositiveSmallIntegerField(choices=[(1, 'New'), (2, 'Second Hand'), (3, 'Old')])),
                ('months_old', models.PositiveSmallIntegerField()),
                ('quantity_required', models.PositiveSmallIntegerField()),
                ('max_price', models.PositiveIntegerField()),
                ('more_info', models.CharField(max_length=512)),
                ('item_status', models.PositiveSmallIntegerField(choices=[(1, 'pending'), (2, 'active'), (3, 'sold'), (4, 'unsold')])),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='users.User')),
            ],
        ),
    ]
