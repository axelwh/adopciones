# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2023-05-18 21:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0005_persona_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='imagen',
        ),
    ]
