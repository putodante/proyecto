# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 10:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesores', '0006_profesores_calle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profesores',
            name='calle',
        ),
    ]
