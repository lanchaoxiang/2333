# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-05-17 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cate_choice',
            field=models.CharField(blank=True, choices=[('hot', 'hot'), ('best', 'best')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='vote',
            field=models.CharField(blank=True, choices=[('dislike', 'dislike'), ('like', 'like'), ('normal', 'normal')], max_length=10, null=True),
        ),
    ]
