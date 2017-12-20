# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZeaBelleGoods', '0004_auto_20171220_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='quantity',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]