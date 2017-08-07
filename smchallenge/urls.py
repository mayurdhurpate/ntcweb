from django.conf.urls import url
from django.contrib import admin
import smchallenge.views as views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]