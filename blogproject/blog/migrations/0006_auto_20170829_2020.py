# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170829_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(),
        ),
    ]
