# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 21:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintSystem', '0009_auto_20160331_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorityWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Vinay Rebeiro', max_length=40)),
                ('email', models.CharField(default='Vinay@iitd.ac.in', max_length=40)),
                ('userName', models.CharField(default='vinay', max_length=40, unique=True)),
                ('password', models.CharField(default='vinay', max_length=40)),
                ('type', models.CharField(choices=[('Electrician', 'Electrician'), ('Plumber', 'Plumber'), ('Carpenter', 'Carpenter'), ('Security', 'Security'), ('CSC', 'Computer Services Center'), ('NA', 'Not an authority worker')], default='NA', max_length=12)),
                ('contactNo', models.BigIntegerField(default=9910272880)),
            ],
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='status',
        ),
        migrations.AddField(
            model_name='complaints',
            name='status_AS',
            field=models.BooleanField(choices=[(False, 'Unassigned to any authority personnel'), (True, 'Assigned to an authority personnel')], default=False),
        ),
        migrations.AddField(
            model_name='complaints',
            name='status_RU',
            field=models.BooleanField(choices=[(True, 'Complaint Resolved'), (False, 'Complaint yet to be Resolved')], default=False),
        ),
        migrations.AddField(
            model_name='users',
            name='contactNo',
            field=models.BigIntegerField(default=9910272880),
        ),
        migrations.AlterField(
            model_name='users',
            name='residency',
            field=models.CharField(choices=[('Karakoram', 'Karakoram'), ('Nilgiri', 'Nilgiri'), ('Himadri', 'Himadri'), ('Jwalamukhi', 'Jwalamukhi'), ('Udaigiri', 'Udaigiri'), ('Appartment', 'Appartment'), ('Individual', 'Individual Housing')], default='Karakoram', max_length=25),
        ),
        migrations.AlterField(
            model_name='users',
            name='typeOfUser',
            field=models.CharField(choices=[('Student', 'Student'), ('Warden', 'Warden'), ('Faculty', 'Faculty')], default='Student', max_length=20),
        ),
        migrations.AddField(
            model_name='complaints',
            name='assignedWorker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ComplaintSystem.AuthorityWorker'),
        ),
    ]
