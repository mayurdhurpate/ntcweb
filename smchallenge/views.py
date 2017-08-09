# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def register_submit(request):
    print(request.POST['inputEmail'])
    email = request.POST['inputEmail']
    password = request.POST['inputPassword']
    name = request.POST['inputName']
    contact = request.POST['inputContact']
    user = User.objects.create_user(email, email, password)
    user.first_name = name
    participant = Participant()
    participant.contact = contact
    user.participant = participant
    user.save()
    participant.save()
    return JsonResponse({'result':True, 'email':email})