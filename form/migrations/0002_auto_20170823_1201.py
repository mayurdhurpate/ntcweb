# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='institute',
            name='course_id',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institute',
            name='mou',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
