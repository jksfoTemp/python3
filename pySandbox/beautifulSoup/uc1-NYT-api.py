#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import requests

KEY = "YOUR_KEY_HERE"
date = datetime.datetime.now().strftime("%Y%m%d")

BASE_REQUEST = (
        "https://api.nytimes.com/svc/search/v2/articlesearch.json"
        # https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key=wXyrr9dEtis3Q0FoY1Cj9cQbOlN4aMrV
)

payload = {
  	"api-key": "wXyrr9dEtis3Q0FoY1Cj9cQbOlN4aMrV",
  	"begin_date": 20120101,
  	"end_date": 20120102,
  	"q": "Silly"
}

# r = requests.get(BASE_REQUEST, param=payload)
r = requests.get(BASE_REQUEST, payload)

if r.status_code == 200:
    print(r.json())
else:  
  #  print ("Bad request:" + str(r.status_code)) 
  print ("Bad request:" + str(r)) 

