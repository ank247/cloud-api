# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam_Type', models.CharField(max_length=30)),
            ],
        ),
    ]
