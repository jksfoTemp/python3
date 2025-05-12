#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

r = requests.get(
    'https://en.wikipedia.org/wiki/Web_scraping')

if r.status_code == 200:
	print(r.text)
else: 
  print("Fail" + r) 

  