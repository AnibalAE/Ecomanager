# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-01 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171001_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='Energia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on', models.DateTimeField()),
                ('off', models.DateTimeField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='predio',
            name='off',
            field=models.DateTimeField(default='22:00'),
        ),
        migrations.AddField(
            model_name='predio',
            name='on',
            field=models.DateTimeField(default='08:00'),
        ),
        migrations.AddField(
            model_name='energia',
            name='predio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predio', to='blog.Predio'),
        ),
    ]
