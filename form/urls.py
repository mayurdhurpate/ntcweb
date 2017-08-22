from django.conf.urls import url
from django.contrib import admin
import form.views as views

urlpatterns = [

    url(r'coordinator/$', views.coordinator_form, name='coordinator_form'),
    url(r'coordinator-submit/$', views.form_submit, name='form_submit'),

]