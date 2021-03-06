from models.stats_data import Data, get_Query
from models.urls import srcmap, urllist
from models.tzinfo import GMT2

import json

from datetime import datetime, timedelta

from google.appengine.api import memcache


def convert_to_epoch(time):
    epoch = datetime(1970, 1, 1)
    return int((time - epoch).total_seconds())*1000

def get_data(timeperiod, src, newstype, limit):
    data = (
        get_Query(Data).filter('datetime >', timeperiod)
        .filter('src =', src).filter('newstype =', newstype)
        .fetch(limit = limit)
        )
    return data

def create_series(data, container, key):
    for d in data:
        container[key].append([
              convert_to_epoch(d.datetime + timedelta(hours = 2)),
              d.value
            ])
        

def _generate_data(days, minutes):
    
    timeperiod = datetime.now(GMT2()) - timedelta(days = days) - timedelta(minutes = minutes)

    all_news = []    
    by_newstype = dict()
    by_src = dict()
    
    data = get_data(timeperiod, None, None, 6)
    for d in data:
        all_news.append([
            convert_to_epoch(d.datetime + timedelta(hours = 2)),
            d.value
                    ])
    
    for newstype in urllist:
        data = get_data(timeperiod, None, newstype, 100)        
        by_newstype[newstype] = []        
        create_series(data, by_newstype, newstype)        
        

    for src in srcmap.values():
        data = get_data(timeperiod, src, None, 1000)        
        by_src[src] = []        
        create_series(data, by_src, src)        
    
    charts = dict()
    charts['chart'] = {
                       'data': all_news,
                       'label': 'Tum Kaynaklar'}
    for newstype in by_newstype:
        charts[newstype] = {
                            'data': by_newstype[newstype],
                            'label': newstype}
                                         
    for src in by_src:
        charts[src] = {
                       'data': by_src[src],
                       'label': src}


    """
    json_str = json.dumps({
        'chart': {
            'tooltip': 'Alinan haber sayisi %1: %2',
            'data': all_news,
            'label': 'Tum Kaynaklar'
             },
        'chart2':{
            'tooltip': 'Alinan haber sayisi %1: %2',
            'data': all_news,
            'label': 'Haber Turune Gore'
        })
    """

    json_str = json.dumps(charts)    
    
    memcache.add("json_str", json_str, 600)
        
    return json_str
  
      
def generate_data(days, minutes):
    json_str = memcache.get("json_str")
    if json_str == None:
        return _generate_data(days, minutes)
    return json_str  
    
