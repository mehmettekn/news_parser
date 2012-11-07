from google.appengine.ext import db
from main import *

class News_Cluster(db.Model):
    name = db.StringProperty()
    news_type = db.StringProperty()

def cluster_key(name = 'default'):
    return db.Key.from_path('clusters', name)
