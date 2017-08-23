from django import forms
from django.forms import ModelForm
from form.models import *
from django.utils.translation import ugettext_lazy as _

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class InstituteForm(ModelForm):
    class Meta:
        model = Institute
        fields = ['name', 'address', 'city', 'district', 'state',\
        'course','course_id', 'talk', 'venue','mou', 'other']
        labels = {
            'name': _('College Name'),
            'course': _('Regular YES!+ courses inside the Campus premises '),
            'course_id': _('If Yes, Course ID of the last course taught '),
            'talk': _('Regular Introductory Sessions in the Campus '),
            'venue': _('Use the campus premises only as a venue for other Art of Living Programs '),
            'mou': _('Signed MoU between VVKi/SSPT and the college/university '),
            'other': _('Other Activities '),
        }
