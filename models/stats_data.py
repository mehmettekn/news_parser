from google.appengine.ext import db
from main import *

def data_key(name = 'default'):
    return db.Key.from_path('data', name)

class Data(db.Model):
    value = db.IntegerProperty()    
    newstype = db.StringProperty()
    src = db.StringProperty()    
    datetime = db.DateTimeProperty()
   

class get_Query(db.Query):
    def _filter(self, property_operator, value):
        if not self:
            raise ImplementationError
        if value == None:
            return self
        return self.filter(property_operator, value) 
    
