# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintSystem', '0010_auto_20160401_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaints',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='authorityworker',
            name='type',
            field=models.CharField(choices=[('Electrician', 'Electrician'), ('Plumber', 'Plumber'), ('Carpenter', 'Carpenter'), ('Security', 'Security'), ('CSC', 'Computer Services Center')], default='Electrician', max_length=12),
        ),
    ]