# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models


class DemoModel(models.Model):
    fk = models.ForeignKey(User,
                           on_delete=models.CASCADE,
                           blank=True, null=True)
    char = models.CharField('Chäř', max_length=255)
    integer = models.IntegerField()
    logic = models.BooleanField(default=False)
    null_logic = models.NullBooleanField(default=None)
    date = models.DateField()
    # datetime = models.DateTimeField()
    # time = models.TimeField()
    # decimal = models.DecimalField(max_digits=10, decimal_places=3)
    # email = models.EmailField()
    # float = models.FloatField()
    # bigint = models.BigIntegerField()
    # url = models.URLField()
    # text = models.TextField()
    json = JSONField(blank=True, null=True)
    nullable = models.CharField(max_length=255, null=True, default=None)
    choices = models.IntegerField(choices=((1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3')))

    class Meta:
        app_label = 'demoproject'
