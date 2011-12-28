#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8


from django.conf.urls.defaults import *

import KHID.views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 


urlpatterns = patterns('',
    # mini dashboard for this app
    url(r'^KHID/PatientSymptoms/', v.patientSymptomsView),
    url(r'^KHID/Patients/', v.patientsView),
    url(r'^KHID/Hierarchys/', v.hierarchysView),
    url(r'^KHID/KunitSummary/', v.kunitDashboardView),
 
    url(r'^KHID/WardSummary/', v.wardSummaryView, name='WardSummary'),
 
    url(r'^KHID/Dashboard2/', v.dashboardView),
    url(r'^KHID/test/', v.testView),
    url(r'^$', 'KHID.views.dashboardView'),
)

urlpatterns += staticfiles_urlpatterns()
