# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-05-23 03:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_auto_20180522_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='instationmessage',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes', to='firstapp.Article'),
        ),
        migrations.AlterField(
            model_name='instationmessage',
            name='phone',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='vote',
            field=models.CharField(blank=True, choices=[('dislike', 'dislike'), ('like', 'like'), ('normal', 'normal')], max_length=10, null=True),
        ),
    ]
