from django.db import models


 

class SymptomCount(models.Model):
   name = models.CharField(max_length=100,blank=True,null=True)
   symptomcount = models.IntegerField()
   class Meta:
    db_table = 'KHID_vw_SymptomCount' # db view
    managed = False

class SymptomCountByKUnitBySymptom(models.Model):
   kunitid = models.IntegerField()
   kunitname = models.CharField(max_length=100,blank=True,null=True)
   name = models.CharField(max_length=100,blank=True,null=True)
   symptomcount = models.CharField(max_length=100,blank=True,null=True)
   class Meta:
    db_table = 'KHID_vw_symptomcount_bykunit_bysymptom' # db view
    managed = False

class SymptomCountByWardBySymptom(models.Model):
   wardid = models.IntegerField()
   wardname = models.CharField(max_length=100,blank=True,null=True)
   name = models.CharField(max_length=100,blank=True,null=True)
   symptomcount = models.CharField(max_length=100,blank=True,null=True)
   class Meta:
    db_table = 'KHID_vw_symptomcount_byward_bysymptom' # db view
    managed = False

 



class SymptomCountByKUnit(models.Model):
   
   name = models.CharField(max_length=100,blank=True,null=True)
   symptomcount = models.CharField(max_length=100,blank=True,null=True)
   class Meta:
    db_table = 'KHID_vw_symptomcount_bykunit' # db view
    managed = False

class SymptomCountByWard(models.Model):
   
   name = models.CharField(max_length=100,blank=True,null=True)
   symptomcount = models.CharField(max_length=100,blank=True,null=True)
   class Meta:
    db_table = 'KHID_vw_symptomcount_byward' # db view
    managed = False

class Ward(models.Model): 
     
 
       name =  models.CharField(max_length=100,blank=True,null=True)
       adsID = models.ForeignKey('ADS')
       def __unicode__(self):
        return self.name

class KUnit(models.Model): 
  

       name =  models.CharField(max_length=100,blank=True,null=True)
       wardID    =  models.ForeignKey('Ward')
       def __unicode__(self):
        return self.name

       class Meta:
          verbose_name = "K Unit"

class ADS(models.Model): 
      

       name =  models.CharField(max_length=100,blank=True,null=True)
       def __unicode__(self):
        return self.name

       class Meta:
          verbose_name = "ADS"

class Patient(models.Model):
     patientid = models.CharField(unique=True,max_length=30)
     fname =  models.CharField(max_length=100,blank=True,null=True)
     lname =  models.CharField(max_length=100,blank=True,null=True)
 	
     kUnitID              =  models.ForeignKey('KUnit')
     def __unicode__(self):
        return u"%s %s" % (self.fname,self.lname)
 
 
class PatientSymptom(models.Model):
     patient    =  models.ForeignKey('Patient')
 
     symptomCode  =  models.ForeignKey('SymptomCode')
     dateReported = models.DateField(blank=True,null=True)
     
     class Meta:
          verbose_name = "Patient Symptom"
          ordering = ["dateReported","symptomCode"]

class FAQ(models.Model):
	FAQCode  = models.CharField(max_length=25,blank=True,null=True)
        name =  models.CharField(max_length=100,blank=True,null=True)	
        def __unicode__(self):
         return self.name

        class Meta:
          verbose_name = "FAQ"

class SymptomCode(models.Model):
     symptomCode  = models.CharField(max_length=25,blank=True,null=True)
     name =  models.CharField(max_length=100,blank=True,null=True)
     shortname = models.CharField(max_length=30,blank=True,null=True)
     def __unicode__(self):
        return self.name

     class Meta:
          verbose_name = "Symptom Code"

class FaqRequest(models.Model):
     FAQCode =  models.ForeignKey('FAQ')
     patientID = models.ForeignKey('Patient')
     requestDate = models.DateField(auto_now_add=True)

     class Meta:
          verbose_name = "FAQ Request"



