# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2023-05-18 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_auto_20230517_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(null=True, to='mascota.Vacuna'),
        ),
    ]
