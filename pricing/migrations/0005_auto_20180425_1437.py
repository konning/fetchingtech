# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-25 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pricing', '0004_auto_20180425_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='publish_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
