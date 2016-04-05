# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintSystem', '0006_auto_20160331_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='levelOfComplaint',
            field=models.CharField(choices=[('individualLevel', 'Individual'), ('hostelLevel', 'Hostel'), ('instituteLevel', 'Institute')], max_length=15),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='resolvedDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='title',
            field=models.CharField(help_text='Title of the Complaint', max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='userName',
            field=models.CharField(default='vinay', max_length=40, unique=True),
        ),
    ]
