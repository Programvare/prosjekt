# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='CourseID',
            field=models.CharField(help_text='Use upper case letters followed by 4 numbers: Example: TDT4100', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='Term',
            field=models.CharField(blank=True, help_text='Please use the following format: <season> <year>. Example: Spring 2017', max_length=20),
        ),
    ]