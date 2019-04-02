# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-02 07:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestLive', '0017_upload_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registratio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=1000)),
                ('Mobile_no', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='use',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Email_Address', models.CharField(max_length=100)),
                ('Contact_Detail', models.DecimalField(decimal_places=0, max_digits=10)),
                ('Profile_Pic', models.ImageField(upload_to=b'')),
                ('Temporary_Address', models.CharField(max_length=150)),
                ('PAN', models.DecimalField(decimal_places=0, max_digits=16)),
                ('Aadhar_Card', models.DecimalField(decimal_places=0, max_digits=16)),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
            ],
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
