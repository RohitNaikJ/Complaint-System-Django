# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintSystem', '0014_auto_20160410_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorityworker',
            name='type',
            field=models.CharField(choices=[('electricity', 'Electrician'), ('plumber', 'Plumber'), ('carpenter', 'Carpenter'), ('security', 'Security'), ('csc', 'Computer Services Center')], default='electrician', max_length=12),
        ),
    ]
