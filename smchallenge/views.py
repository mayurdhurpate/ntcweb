# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from smchallenge.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'base.html')

def signup(request):
    return render(request, 'base_signup.html')

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

def loginuser(request):
    return render(request, 'base_login.html')

def login_submit(request):
    print(request.POST['inputEmail'])
    email = request.POST['inputEmail']
    password = request.POST['inputPassword']
    user = authenticate(request,username=email,password=password)
    if user is not None:
        login(request,user)
        return JsonResponse({'result':True, 'email':email})
    else:
        return JsonResponse({'result':False, 'email':email})
         
@login_required
def dashboard(request):
    tasks = Task.objects.order_by('-number')
    print(tasks[0])
    return render(request, 'base_dashboard.html', {'tasks':tasks})

@login_required
def submit(request,number):
    print(number)
    a = 'a'
    return render(request, 'base_submit.html', {'number':number})

@login_required
def leaderboard(request):
    users = User.objects.all()
    userData = []
    for user in users:
        u = {}
        u['name'] = user.first_name
        u['score'] = 0
        scores = Score.objects.filter(user=user)
        for score in scores:
            u['score'] = u['score'] + score.score
        u['taskCount'] = len(scores)
        userData.append(u)

    print(userData)
    return render(request, 'base_leaderboard.html', {'userData':userData})

@login_required
def submit_submit(request,number):
    print(request.POST['inputScore'])
    score = request.POST['inputScore']
    link = request.POST['inputLink']
    user = request.user
    task = Task.objects.get(number=number)
    try:
        scoreObject = Score.objects.get(user=user, task=task)
    except Score.DoesNotExist:
        scoreObject = Score()
        scoreObject.user = user
        scoreObject.task = task
    scoreObject.score = score
    scoreObject.save()
    return JsonResponse({'result':True, 'email':user.email})

#1174