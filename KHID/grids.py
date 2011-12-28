from jqgrid import *
from json_encode import *
from .models import *
from django.core.urlresolvers import reverse
from django.utils.functional import lazy 

class WardGrid(JqGrid):
    model = SymptomCountByWardBySymptom 
    fields = ['wardname', 'name', 'symptomcount'] # optional 
    
    url = ("wardSummary") 
    caption = 'My First Grid' # optional
   
def get_config(self, as_json=True):
    config = self.get_default_config()
    config.update({
        
 
        'caption': self.get_caption(),
         
     })


