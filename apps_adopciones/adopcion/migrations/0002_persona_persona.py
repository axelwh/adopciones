# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2023-05-17 21:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_auto_20230517_2153'),
        ('adopcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mascota.Mascota'),
        ),
    ]