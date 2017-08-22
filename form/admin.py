# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from form.models import *


admin.site.register(Coordinator)
admin.site.register(Institute)