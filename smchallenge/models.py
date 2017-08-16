# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    score = models.IntegerField(default=0)

class Task(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    number = models.IntegerField()
    def __unicode__(self):
        return u"Task: %s" % self.title

class Score(models.Model):
    user = models.ForeignKey(User)
    task = models.ForeignKey(Task)
    score = models.IntegerField(default=0)
    def __unicode__(self):
        return u"Score: %s" % self.user.username