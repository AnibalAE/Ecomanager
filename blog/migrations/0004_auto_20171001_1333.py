# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-01 16:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171001_1311'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Energia',
            new_name='Agendamento',
        ),
    ]
