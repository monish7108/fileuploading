# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cust_details',
            fields=[
                ('cust_account_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='cust_account_id')),
                ('cust_name', models.CharField(max_length=25, verbose_name='cust_name')),
                ('cust_address', models.TextField(verbose_name='cust_address')),
                ('cust_dob', models.DateField(auto_now_add=True, verbose_name='cust_dob')),
                ('cust_email', models.EmailField(max_length=254)),
                ('cust_balance', models.IntegerField()),
                ('cust_picture', models.FileField(upload_to='pictures/')),
            ],
        ),
    ]
