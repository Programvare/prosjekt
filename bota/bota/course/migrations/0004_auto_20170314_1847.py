# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-14 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='delivery_deadline',
            field=models.DateTimeField(help_text='Please use the following format: <em>YYYY-MM-DD hh:mm</em>'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='demo_deadline',
            field=models.DateTimeField(help_text='Please use the following format: <em>YYYY-MM-DD hh:mm</em>'),
        ),
    ]
