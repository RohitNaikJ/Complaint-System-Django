# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 04:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintSystem', '0012_auto_20160407_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='complaint_roomNo',
            field=models.CharField(blank=True, default='0', max_length=40, null=True),
        ),
    ]
