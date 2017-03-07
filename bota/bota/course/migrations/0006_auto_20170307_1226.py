# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20170306_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='CourseID',
            field=models.CharField(help_text='Use upper case letters followed by 4 numbers: Example: TDT4100', max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='Description',
            field=models.CharField(blank=True, default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='course',
            name='Nickname',
            field=models.CharField(blank=True, default='', help_text='Please enter a nickname for the course if possible', max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='Term',
            field=models.CharField(help_text='Please use the following format: <season> <year>. Example: Spring 2017', max_length=20),
        ),
        migrations.AlterField(
            model_name='tatime',
            name='date',
            field=models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.'),
        ),
        migrations.AlterField(
            model_name='tatime',
            name='end_time',
            field=models.TimeField(help_text='Please use the following format: <em>hh:mm</em>'),
        ),
        migrations.AlterField(
            model_name='tatime',
            name='start_time',
            field=models.TimeField(help_text='Please use the following format: <em>hh:mm</em>'),
        ),
    ]
