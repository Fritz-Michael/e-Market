# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ZeaBelleGoods', '0002_auto_20171220_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
