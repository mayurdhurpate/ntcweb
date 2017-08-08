from django.conf.urls import url
from django.contrib import admin
import smchallenge.views as views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'register/$', views.signup, name='signup'),
    url(r'register-submit/$', views.register_submit, name='register_submit'),
]