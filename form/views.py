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
    return render(request, 'base_index.html')

def coordinator_form(request):
    if request.method=='POST':
        teacher_code = request.POST['inputTeacherCode']
        coordinator = Coordinator.objects.create(teacherCode=teacher_code)
        coordinator.save()
        form = InstituteForm()
        return render(request, 'base_form.html',{'form':form,'teacher_code':teacher_code})

def form_submit(request,teacher_code):
    if request.method == 'POST':
        coordinator = Coordinator.objects.filter(teacherCode=teacher_code)[0]
        form = InstituteForm(request.POST)
        new_institute = form.save(commit=False)
        new_institute.coordinator = coordinator
        new_institute.save()

        return JsonResponse({'result':True, 'teacher_code':teacher_code})
