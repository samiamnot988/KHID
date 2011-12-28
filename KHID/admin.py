#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

from django.contrib import admin 
from models import *

 

class WardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'adsID')

class FAQAdmin(admin.ModelAdmin):
    list_display =('FAQCode','name')

class SymptomAdmin(admin.ModelAdmin):
    list_display = ('symptomCode','name','shortname')

class KUnitAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'wardID')

class FaqRequestAdmin(admin.ModelAdmin):
    list_display = ('FAQCode','patientID','requestDate')
 
class ADSAdmin  (admin.ModelAdmin):
    list_display = ('id','name')

class PatientAdmin(admin.ModelAdmin):
  list_display = ('id','patientid','fname', 'lname','kUnitID')

 
class PatientSymptomAdmin(admin.ModelAdmin):
   list_display = ('patient','symptomCode', 'dateReported')                

admin.site.register(Ward, WardAdmin)
admin.site.register(KUnit, KUnitAdmin)
admin.site.register(ADS,ADSAdmin)
admin.site.register(FAQ,FAQAdmin)
admin.site.register(PatientSymptom, PatientSymptomAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(FaqRequest, FaqRequestAdmin)
admin.site.register(SymptomCode, SymptomAdmin)

