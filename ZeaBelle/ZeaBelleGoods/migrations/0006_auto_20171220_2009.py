# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZeaBelleGoods', '0005_products_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='resources'),
        ),
    ]
