# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('unit_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('retail_price', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]