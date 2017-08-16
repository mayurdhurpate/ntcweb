# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 12:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smchallenge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('content', models.TextField()),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='score',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smchallenge.Task'),
        ),
        migrations.AddField(
            model_name='score',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]