# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Coordinator(models.Model):
    teacherCode = models.CharField(max_length=10)
    def __unicode__(self):
        return u"%s" % self.teacherCode

class Institute(models.Model):
    coordinator = models.ForeignKey(Coordinator)
    name = models.CharField(max_length=500)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    course = models.BooleanField()
    talk = models.BooleanField()
    venue = models.BooleanField()
    other = models.TextField(blank=True)
    def __unicode__(self):
        return u"%s" % self.name
