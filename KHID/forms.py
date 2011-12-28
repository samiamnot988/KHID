from django import forms
from .models import *
from django.forms import ModelForm, ModelChoiceField
from django.forms.extras.widgets import SelectDateWidget
from django.forms.fields import DateField, ChoiceField  
from django.forms.widgets import  Select, CheckboxSelectMultiple

TIME_CHOICES = (
        (u'All', u'All'),
        (u'Year', u'Year'),
        (u'Month', u'Month'),
 

    )

YEAR_CHOICES = (
        (u'2010', u'2010'),
        (u'2011', u'2011'),
        (u'2012', u'2012'),
        (u'2013', u'2013'),

    )

MONTH_CHOICES = (
        (u'1', u'January'),
        (u'2', u'February'),
        (u'3', u'March'),
        (u'4', u'April'),
        (u'5', u'May'),
        (u'6', u'June'),
        (u'7', u'July'),
        (u'8', u'August'),
        (u'9', u'September'),
        (u'10', u'October'),
        (u'11', u'November'),
        (u'12', u'December')

)

 
 
class PatientSymptomForm(forms.Form):
     
    patient = ModelChoiceField(queryset=Patient.objects.all().order_by('fname', 'lname'),required=False)

class KunitSummaryForm(forms.Form):
     
    kunit = ModelChoiceField(queryset=KUnit.objects.all(),required=False)

class WardSummaryForm(forms.Form):
     
    ward = ModelChoiceField(queryset=Ward.objects.all(),required=False)
  
class DashboardForm(forms.Form):
    time = forms.ChoiceField(choices=TIME_CHOICES, required=False,widget=forms.Select(attrs={'onchange':'ShowHideYear();'}))
    year = ChoiceField(widget=Select, choices=YEAR_CHOICES, required=False)
    month = ChoiceField(widget=Select, choices=MONTH_CHOICES, required=False)
 
