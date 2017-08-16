from django.conf.urls import url
from django.contrib import admin
import smchallenge.views as views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'register/$', views.signup, name='signup'),
    url(r'register-submit/$', views.register_submit, name='register_submit'),

    url(r'login/$', views.loginuser, name='login'),
    url(r'login-submit/$', views.login_submit, name='login_submit'),

    url(r'dashboard/$', views.dashboard, name='dashboard'),
    url(r'leaderboard/$', views.leaderboard, name='leaderboard'),

    url(r'^submit/([0-9]{1,2})/$', views.submit, name='submit'),
    url(r'submit-submit/([0-9]{1,2})/$', views.submit_submit, name='submit_submit'),
]