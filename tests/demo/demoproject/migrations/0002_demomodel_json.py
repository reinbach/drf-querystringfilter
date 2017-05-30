# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-29 18:34
from __future__ import unicode_literals
import django
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoproject', '0001_initial'),
    ]

    if django.VERSION >= (1,9):
        from django.contrib.postgres.fields.jsonb import JSONField
    else:
        from django.db.models import TextField as JSONField
    operations = [
            migrations.AddField(
                model_name='demomodel',
                name='json',
                field=JSONField(blank=True, null=True),
            ),
        ]