# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profesores', '0004_auto_20171117_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='materias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.IntegerField()),
                ('profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profesores.profesores')),
            ],
        ),
    ]