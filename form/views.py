# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from form.models import *
from django.contrib.auth.decorators import login_required
from form.forms import InstituteForm

# Create your views here.
def home(request):
    return render(request, 'base.html')

def coordinator_form(request):
    form = InstituteForm()
    return render(request, 'base_form.html',{'form':form})

def form_submit(request):
    if request.method == 'POST':
        form = InstituteForm(request.POST)
        new_institute = form.save(commit=False)
        new_institute.coordinator = Coordinator.objects.all()[0]
        new_institute.save()

    return JsonResponse({'result':True, 'name':new_institute.name})
