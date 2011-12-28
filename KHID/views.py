
from datetime import *
import os,sys,string
import csv
from django.db import models
from django.http import HttpResponse

from django.template import RequestContext
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.utils.functional import lazy 
from .models import *
import gviz_api 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import *

from jqgrid import *
from json_encode import *
from grids import *

def patientsView(req):
   template_name="Patients.html"




   patiententries = Patient.objects.all()

   context = {'patients': patiententries}
   return render_to_response(template_name, context,
                              context_instance=RequestContext(req))
 

def hierarchysView(req):
   template_name="Hierarchy.html"
   wardentries = Ward.objects.all()
   adsentries = ADS.objects.all()
   kUnitentries = KUnit.objects.all()
   
   context = {'wards': wardentries, 'adss': adsentries, 'kunits': kUnitentries }
   return render_to_response(template_name, context,
                              context_instance=RequestContext(req))

def patientSymptomsView(req):
   template_name="PatientSymptoms.html"
   initialpatient = None
   initialpatient = Patient.objects.get(id=1)
   patients = Patient.objects.get(pk=1)
   patiententries = PatientSymptom.objects.all()
 
   form = PatientSymptomForm(initial={'patient':initialpatient}) 
   if req.method == 'POST':
        form = PatientSymptomForm( req.POST or None)

   if form.is_valid():
          selectedpatient = form.cleaned_data['patient']

         
          patients = Patient.objects.get(pk=selectedpatient.pk) 



   context = {'patients': patients,'form':form}
   return render_to_response(template_name, context,
                              context_instance=RequestContext(req))
@csrf_exempt
def wardSummaryView(req):
   
      from django.db import connection, transaction
      cursor = connection.cursor()
      template_name="WardSummary.html"
      initialward = None
      
      ward = None
      sql = None 
      initialward = Ward.objects.get(id=1)
      symCountByWard= SymptomCountByWardBySymptom.objects.filter(wardid__exact=initialward.pk)
      form = WardSummaryForm(initial={'ward':initialward}) 
      ward = initialward
      if req.method == 'POST':
        form = WardSummaryForm( req.POST or None)

        if form.is_valid():
          ward = form.cleaned_data['ward']

         
          symCountByWard = SymptomCountByWardBySymptom.objects.filter(wardid__exact=ward.pk)
          #sql = connection.queries
      context = {'symcountbywardbysymptom':symCountByWard, 'form':form,  'ward':ward, 'sql':sql}
      return render_to_response(template_name,context,context_instance=RequestContext(req))
 


def kunitDashboardView(req):
   
      from django.db import connection, transaction
      cursor = connection.cursor()
      template_name="KunitSummary.html"
      initialkunit = None
      
      kunit = None
      sql = None 
      initialkunit = KUnit.objects.get(id=1)
      symCountByKunit= SymptomCountByKUnitBySymptom.objects.filter(kunitid__exact =initialkunit.pk)
      form = KunitSummaryForm(initial={'kunit':initialkunit}) 
      kunit = initialkunit
      if req.method == 'POST':
        form = KunitSummaryForm( req.POST or None)

        if form.is_valid():
          kunit = form.cleaned_data['kunit']

         
          symCountByKunit = SymptomCountByKUnitBySymptom.objects.filter(kunitid__exact=kunit.pk)
          #sql = connection.queries
      context = {'symcountbykunitbysymptom':symCountByKunit, 'form':form,  'kunit':kunit, 'sql':sql, 'initialkunit':initialkunit}
      return render_to_response(template_name,context,context_instance=RequestContext(req))
  

def testView(req):
   template_name="test.html"
   context = {}
   return render_to_response(template_name,context,context_instance=RequestContext(req))



@csrf_exempt
def dashboardView(req):
      from django.db import connection, transaction
      cursor = connection.cursor()
      template_name="Dashboard2.html"
      form = DashboardForm() 
       
      time = None
      
      symcount = SymptomCount.objects.all()
      symCountByWard = SymptomCountByWard.objects.all()
      symCountByKunit = SymptomCountByKUnit.objects.all()
  

      if req.method == 'POST':
        form = DashboardForm(req.POST or None)

        if form.is_valid():
          time = form.cleaned_data['time']
          year = form.cleaned_data['year']
          month = form.cleaned_data['month']
      	
        if time == 'Year':
          
          cursor.execute("""select '1' AS id,c.name AS  name ,
                        count(*) AS  symptomcount 
                       from (KHID_patientsymptom  p  
                       join  KHID_symptomcode   c ) 
                       where ( p.symptomCode_id  = c.symptomCode) 
                       and YEAR(dateReported) = %s
                       group by p.symptomCode_id""",[int(year)]);
          symcount = dictfetchall(cursor)

	  cursor.execute("""select '1' AS `id`,
			`w`.`name` AS `name`,
			count(0) AS `symptomcount` 
			from ((((`KHID_patientsymptom` `p` 
			join `KHID_symptomcode` `c`) 
			join `KHID_ward` `w`) 
			join `KHID_patient` `pa`) 
			join `KHID_kunit` `k`) 
			where ((`p`.`symptomCode_id` = `c`.`symptomCode`) 
			and (`pa`.`id` = `p`.`patient_id`) 
			and (`pa`.`kUnitID_id` = `k`.`id`) 
			and (`k`.`wardID_id` = `w`.`id`)) 
			and YEAR(p.dateReported) = %s
			group by `w`.`id`""",[int(year)]);

          symCountByWard = dictfetchall(cursor)
 
          cursor.execute("""select '1' AS `id`,
		`k`.`name` AS `name`,
		count(0) AS `symptomcount` 
		from (((`KHID_patientsymptom` `p` 
		join `KHID_symptomcode` `c`) 
		join `KHID_kunit` `k`) 
		join `KHID_patient` `pa`) 
		where ((`p`.`symptomCode_id` = `c`.`symptomCode`) 
		and (`pa`.`id` = `p`.`patient_id`) 
		and (`pa`.`kUnitID_id` = `k`.`id`)) 
		and YEAR(dateReported) = %s
		group by `pa`.`kUnitID_id`""",[int(year)])

          symCountByKunit = dictfetchall(cursor)

        elif time == 'Month':
          cursor.execute("""select '1' AS id,c.name AS  name ,
                        count(*) AS  symptomcount 
                       from (KHID_patientsymptom  p  
                       join  KHID_symptomcode   c ) 
                       where ( p.symptomCode_id  = c.symptomCode) 
                       and YEAR(dateReported) = %s
                       and MONTH(dateReported) = %s
                       group by p.symptomCode_id""",[int(year),int(month)])
          symcount = dictfetchall(cursor)

	  cursor.execute("""select '1' AS `id`,
				`k`.`name` AS `name`,
				count(0) AS `symptomcount` 
				from (((`KHID_patientsymptom` `p` 
				join `KHID_symptomcode` `c`) 
				join `KHID_kunit` `k`) 
				join `KHID_patient` `pa`) 
				where ((`p`.`symptomCode_id` = `c`.`symptomCode`) 
				and (`pa`.`id` = `p`.`patient_id`) 
				and (`pa`.`kUnitID_id` = `k`.`id`)) 
				and YEAR(dateReported) = %s
				and MONTH(dateReported) = %s
				group by `pa`.`kUnitID_id`""",[int(year),int(month)])
          symCountByKunit = dictfetchall(cursor)

          cursor.execute("""select '1' AS `id`,
			`w`.`name` AS `name`,
			count(0) AS `symptomcount` 
			from ((((`KHID_patientsymptom` `p` 
			join `KHID_symptomcode` `c`) 
			join `KHID_ward` `w`) 
			join `KHID_patient` `pa`) 
			join `KHID_kunit` `k`) 
			where ((`p`.`symptomCode_id` = `c`.`symptomCode`) 
			and (`pa`.`id` = `p`.`patient_id`) 
			and (`pa`.`kUnitID_id` = `k`.`id`) 
			and (`k`.`wardID_id` = `w`.`id`)) 
			and YEAR(p.dateReported) = %s
                        and MONTH(p.dateReported) = %s
			group by `w`.`id`""",[int(year),int(month)])
          symCountByWard = dictfetchall(cursor)
        else:
           
          cursor.execute("""select * FROM KHID.KHID_vw_SymptomCount""")
          symcount = dictfetchall(cursor)
          cursor.execute("""select * FROM KHID.KHID_vw_symptomcount_byward""")
	  symCountByWard = dictfetchall(cursor)
          cursor.execute("""select * FROM KHID.KHID_vw_symptomcount_bykunit""")
	  symCountByKunit = dictfetchall(cursor)	  
           

     
      context = { 'form': form, 'symcount': symcount, 'symCountByKunit':symCountByKunit, 'symCountByWard': symCountByWard, 'Time':time}
      
      return render_to_response(template_name, context,
                              context_instance=RequestContext(req))



def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
  
