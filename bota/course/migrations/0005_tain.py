# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-21 14:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0004_auto_20170221_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='TAin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
