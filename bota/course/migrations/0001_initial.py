# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 18:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.CharField(max_length=7)),
                ('Description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=45)),
                ('LastName', models.CharField(max_length=45)),
                ('Role', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='takes',
            name='CourseID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.User'),
        ),
        migrations.AddField(
            model_name='takes',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
    ]
