#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from rapidsms.apps.base import AppBase
from KHID.models import *
import datetime

class App(AppBase):
    """
    Receive any message. 
    """

    def handle(self, message):

        messageArray = message.text.split()
        if messageArray[0] == "50":
           kunit = KUnit.objects.filter(pk=messageArray[1])
           if len(kunit) == 0:
              message.respond("A KUnit with the ID of " + str(messageArray[1]) + " does not exist.")
           else:
              if len(messageArray) == 4:
                patient = Patient.objects.filter(lname__exact=messageArray[3]).filter(fname__exact = messageArray[2]) 
                if len(patient) == 0:
                  p = Patient(fname = messageArray[2],lname = messageArray[3], kUnitID_id = messageArray[1])
                  p.save()
                  message.respond("Patient with the name " + messageArray[2] + " " + messageArray[3] + " has been created with the ID " + str(p.id) + ".")
                else:
                  patient = patient[0]
                  message.respond("Patient with the name " + patient.fname + " " + patient.lname + " already exists with the ID " + str(patient.id) + ".")
              elif len(messageArray) == 3:
                  patient = Patient.objects.filter(fname__exact = messageArray[2]) 
                  if len(patient) == 0:
                    p = Patient(fname = messageArray[2],kUnitID_id = messageArray[1])
                    p.save()
                    message.respond("Patient with the name " + messageArray[2] + " has been created with the ID " + str(p.id) + ".")
                  else:
                    patient = patient[0]
                    message.respond("Patient with the name " + patient.fname + " already exists with the ID " + str(patient.id) + ".")
 
        elif messageArray[0] == "70":
          ads = ADS.objects.filter(pk = messageArray[1])
          if len(ads) == 0:
             message.respond("A ADS with the ID of " + str(messageArray[1]) + " does not exist.")
          else:
             if len(messageArray) == 4:
               name2 =  messageArray[2] + " " + messageArray[3]
             else:
               name2 = messageArray[2]
             ward = Ward.objects.filter(name__exact=name2)
             if len(ward) == 0:
                w = Ward(name = name2, adsID_id = messageArray[1] )
                w.save()
                message.respond("A Ward with the name " + name2 + " has been created with the ID " + str(w.id) + ".")
             else:
                ward = ward[0]
                message.respond("A Ward with the name " + ward.name + " already exists with the ID " + str(ward.id) + ".")
        elif messageArray[0] == "80":
          w = Ward.objects.filter(pk=messageArray[1])
          if len(w) == 0:
             message.respond("A Ward with the ID of " + str(messageArray[1]) + " does not exist.")
          else:
             if len(messageArray) == 4:
               name2 =  messageArray[2] + " " + messageArray[3]
             else:
               name2 = messageArray[2]
             kunit = KUnit.objects.filter(name__exact=name2)
             if len(kunit) == 0:
                k = KUnit(name = name2, wardID_id = messageArray[1] )
                k.save()
                message.respond("A Kunit with the name " + name2 + " has been created with the ID " + str(k.id) + ".")
             else:
                kunit = kunit[0]
                message.respond("A Kunit with the name " + kunit.name + " already exists with the ID " + str(kunit.id) + ".")
        elif messageArray[0] == "60":
          if len(messageArray) == 3:
            name2 =  messageArray[1] + " " + messageArray[2]
          else:
            name2 = messageArray[1]

          ads = ADS.objects.filter(name__exact=name2)
          if len(ads) == 0:
            a = ADS(name = name2)
            a.save()
            message.respond("An ADS with the name "+name2 + " has been created with the ID " + str(a.id) + ".")
          else:
            ads = ads[0]
            message.respond("An ADS with the name " + name2 + " already exists with the ID " + str(ads.id) + ".")
        elif messageArray[0] == "99":
          patient = Patient.objects.filter(pk=messageArray[1])
          if len(patient) == 0:
             message.respond("A Patient with the ID " + str(messageArray[1] )+ " does not exist.")
          else:
             if '-' in (messageArray[len(messageArray)-1]):
               dateR = messageArray[len(messageArray)-1]
               lastSymptomCodeIndex = (len(messageArray)-2)
                
             else:
               dateR = datetime.datetime.now()
               lastSymptomCodeIndex = len(messageArray)
                
             i  = 2
             while i <= lastSymptomCodeIndex:
                  
                 sym = SymptomCode.objects.filter(pk=messageArray[i])
                 if len(sym) == 0:
                   message.respond("A Symptom Code with the ID " + str(messageArray[i]) + " does not exist.")
                 else:
                   ps = PatientSymptom(patient_id = messageArray[1], symptomCode_id = messageArray[i], dateReported =dateR)
                   ps.save()
                   message.respond("A Symptom Code of " + str(messageArray[i]) + " has been inserted for Patient ID " + str(messageArray[1]) + ".")
                 i = i + 1
             

