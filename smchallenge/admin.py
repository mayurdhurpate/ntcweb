# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from smchallenge.models import Participant

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ParticipantInline(admin.StackedInline):
    model = Participant
    can_delete = False
    verbose_name_plural = 'participant'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ParticipantInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)