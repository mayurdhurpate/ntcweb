# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def register_submit(request):
    print(request.POST['inputEmail'])
    return HttpResponse("qq")