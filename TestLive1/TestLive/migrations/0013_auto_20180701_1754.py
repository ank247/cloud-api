# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-01 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestLive', '0012_auto_20180701_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Coupon', models.CharField(max_length=32)),
                ('Draft', models.CharField(max_length=50)),
                ('Cash_Deposit', models.CharField(max_length=50)),
                ('Echallan', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Payments',
        ),
    ]
