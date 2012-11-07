#!/usr/bin/python
# -*- coding: utf-8 -*-



urllist = {
    'news_urls':{
                "http://www.haberturk.com/rss":1, 
                "http://www.milliyet.com.tr/D/rss/rss/RssSD.xml":2,
                "http://www.milliyet.com.tr/D/rss/rss/Rss_24.xml":2,
                "http://www.milliyet.com.tr/D/rss/rss/Rss_2.xml":2,
                "http://rss.hurriyet.com.tr/rss.aspx?sectionId=1":3,
                "http://rss.hurriyet.com.tr/rss.aspx?sectionId=2":3,
                "http://www.sabah.com.tr/rss/SonDakika.xml":4,
                "http://www.radikal.com.tr/d/rss/RssSD.xml":5,
                "http://www.radikal.com.tr/d/rss/Rss_81.xml":5,
                "http://rss.ekolay.net/pages/haber.aspx":6,
                "http://haber.mynet.com/rss/gununozeti":7,
                "http://haber.mynet.com/rss/sondakika":7,
                "http://www.cumhuriyet.com.tr/?xl=rss":8,
                #"http://zaman.com.tr/anasayfa.rss":{},
                #"http://zaman.com.tr/.rss":{},
                "http://www.turkiyegazetesi.com/rss/turkiyerss.aspx":9,
                "http://www.ntvmsnbc.com/id/24928058/device/rss/rss.xml":10,
                "http://www.aksam.com.tr/cache/rss.xml":11,
              },
            
    'sports_urls':{
                   "http://skorer.milliyet.com.tr/d/skorer.xml":2,
                   "http://rss.hurriyet.com.tr/rss.aspx?sectionId=14":3,
                   "http://www.radikal.com.tr/d/rss/Rss_103.xml":5,
                   "http://www.radikal.com.tr/d/rss/Rss_84.xml":5,
                   "http://sabah.com.tr.feedsportal.com/c/33784/f/606060/index.rss":4,
                   "http://rss.ekolay.net/pages/spor.aspx":6,
                   "http://spor.mynet.com/rss":7,
                   #"http://zaman.com.tr/spor.rss":{},
                   "http://www.ntvmsnbc.com/id/24927361/device/rss/rss.xml":10,
                   "http://rss.feedsportal.com/c/32892/f/530173/index.rss":10,
                   "http://fotospor.com/rss/kategori.xml?id=1":12,
                   "http://www.aksam.com.tr/spor-4r.xml":11
                 },

    'economy_urls':{
                   "http://www.milliyet.com.tr/D/rss/rss/Rss_3.xml":2,
                   "http://rss.hurriyet.com.tr/rss.aspx?sectionId=4":3,
                   "http://www.radikal.com.tr/d/rss/Rss_101.xml":5,
                   "http://www.radikal.com.tr/d/rss/Rss_80.xml":5,
                   "http://sabah.com.tr.feedsportal.com/c/33784/f/606057/index.rss":4,
                   "http://www.bigpara.com/rss/gundem.asp":13,
                   "http://finanshaber.mynet.com/rss/gununozeti":7,
                   #"http://zaman.com.tr/ekonomi.rss":{},
                   "http://www.ntvmsnbc.com/id/24927364/device/rss/rss.xml":10,
                   "http://www.ntvmsnbc.com/id/24927367/device/rss/rss.xml":10,
                   "http://www.aksam.com.tr/ekonomi-3r.xml":11
                  },

    "tech_urls": {
                  "http://www.milliyet.com.tr/D/rss/rss/Rss_36.xml":2,
                  "http://rss.hurriyet.com.tr/rss.aspx?sectionId=2158":3,
                  "http://www.radikal.com.tr/d/rss/Rss_117.xml":5,
                  "http://www.sabah.com.tr/rss/Teknoloji.xml":4,
                  #"http://zaman.com.tr/bilisim.rss":{}
                 },






    "health_urls": {
                    "http://www.milliyet.com.tr/D/rss/rss/Rss_31.xml":2,
                    "http://rss.hurriyet.com.tr/rss.aspx?sectionId=2124":3,
                    "http://www.radikal.com.tr/d/rss/Rss_118.xml":5,
                    "http://www.sabah.com.tr/rss/Saglik.xml":4,
                    #"http://zaman.com.tr/ailesaglik.rss":{}
                   }

    }

srcmap = {1:'Haberturk',
          2:'Milliyet',
          4:'Radikal',
          3:'Hurriyet',
          5:'Sabah',
          6:'eKolay',
          7:'MyNet',
          8:'Cumhuriyet',
          9:'Turkiye',
         10:'NtvMsnbc',
         11:'Aksam',
         12:'Fotospor',
         13:'BigPara'
   }

no_image_url = "https://encrypted-tbn1.gstatic.com/images?      q=tbn:ANd9GcTEzsZdA0I-mk9lPYUZaJbJ6rcTYXl53Rv1uin78SRlckU9MwV6Kw"

