# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ComplaintSystem', '0003_users_roomno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title of complaint', max_length=200)),
                ('description', models.TextField(help_text='Enter Complaint Description')),
                ('origin', models.CharField(choices=[('Karakoram', 'Karakoram'), ('Nilgiri', 'Nilgiri'), ('Himadri', 'Himadri'), ('Jwalamukhi', 'Jwalamukhi'), ('Udaigiri', 'Udaigiri'), ('Institute', 'IIT Delhi'), ('Individual House', 'Individual House')], default='Karakoram', max_length=20)),
                ('levelOfComplaint', models.CharField(choices=[('individualLevel', 'individual_level'), ('hostelLevel', 'hostel_level'), ('instituteLevel', 'institute_level')], max_length=15)),
                ('category', models.CharField(choices=[('electricity', 'electricity'), ('plumbing', 'plumbing'), ('carpentry', 'carpentry'), ('sports', 'sports'), ('cultural', 'cultural'), ('library', 'library'), ('csc', 'Computer Services Center'), ('mess', 'mess'), ('security', 'security'), ('others', 'others')], default='others', max_length=15)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('resolvedDate', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='Residency',
        ),
        migrations.AddField(
            model_name='users',
            name='residency',
            field=models.CharField(choices=[('Karakoram', 'Karakoram'), ('Nilgiri', 'Nilgiri'), ('Himadri', 'Himadri'), ('Jwalamukhi', 'Jwalamukhi'), ('Udaigiri', 'Udaigiri'), ('Individual', 'Individual Housing')], default='Karakoram', max_length=25),
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(default='Vinay@iitd.ac.in', max_length=40),
        ),
        migrations.AlterField(
            model_name='users',
            name='roomNo',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(default='vinay', max_length=40, unique=True),
        ),
        migrations.AddField(
            model_name='complaints',
            name='lodgedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComplaintSystem.Users'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComplaintSystem.Users'),
        ),
        migrations.AddField(
            model_name='comments',
            name='complaint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ComplaintSystem.Complaints'),
        ),
    ]
