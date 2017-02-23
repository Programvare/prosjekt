# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 16:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.CharField(max_length=10)),
                ('Name', models.CharField(default=b'TBA', max_length=20)),
                ('Term', models.CharField(default=b'TBA', max_length=10)),
                ('Description', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TAin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TATime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.CharField(help_text=b'E.g.: <em>hh:mm</em>.', max_length=200)),
                ('end_time', models.CharField(help_text=b'E.g.: <em>hh:mm</em>.', max_length=200)),
                ('teaching_assistant', models.CharField(max_length=200)),
                ('room', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
    ]
