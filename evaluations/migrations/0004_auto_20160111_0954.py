# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 08:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluations', '0003_auto_20160111_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='observer',
            old_name='evaluation ended',
            new_name='evaluation_ended',
        ),
        migrations.RenameField(
            model_name='observer',
            old_name='startTime',
            new_name='evaluation_started',
        ),
    ]
