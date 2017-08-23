from django.conf.urls import url
from django.contrib import admin
import form.views as views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'coordinator/$', views.coordinator_form, name='coordinator_form'),
    url(r'coordinator-submit/(?P<teacher_code>[\w-]+)/$', views.form_submit, name='form_submit'),
]