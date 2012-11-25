#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import logging

from google.appengine.api import urlfetch
from google.appengine.api.urlfetch_errors import DeadlineExceededError
from google.appengine.api import memcache

from bs4 import BeautifulSoup

url = "http://pages2.foreks.com/piyasa_verileri/Hisse.asp?char="
chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
         'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'Y', 'Z']

downSymbol = u"▼"
upSymbol = u"▲"
symbol = ""

def generate_imkb_data():
    imkb = dict()
    imkb["ENDEKS"] = []
    result = memcache.get("imkb_json")
    if result:
        return result
    else:   
        for char in chars:
            url_to_parse = url + char
            try:
                page = urlfetch.fetch(url_to_parse).content
            except(DeadlineExceededError):
                continue
            soup = BeautifulSoup(page)
            items = soup.findAll('tr', attrs={'class':'GridText'})
            for item in items:
                value_class = ''            
                dataset = item.findAll('td')
                name = dataset[0].getText()
                ask = (dataset[1].getText())
                change = str(dataset[2].getText())                
                change_value = float(dataset[2].getText())
                
                if change_value > 0:
                    value_class = "UP"
                    symbol = upSymbol
                else:
                    value_class = "DOWN"
                    symbol = downSymbol            
                imkb["ENDEKS"].append({
                    "NAME":name,
                    "ASK": ask,
                    "CHANGE": change,
                    "CLASS" : value_class,
                    "SYMBOL": symbol})
                         
    imkb_json = json.dumps(imkb)
    result = imkb_json
    memcache.add("imkb_json", result, 300)    
    return result

