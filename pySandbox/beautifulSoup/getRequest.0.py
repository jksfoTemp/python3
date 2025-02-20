#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Only using this to download a save a sample page 
  TODO: Should still harden ... main ... error handling 
  TODO: Should parameterize for url and output file 
  Janky but it works : getRequest.0.py 
  Output file: sampleFile.html
"""

import requests

# Get response object; Switch for the file "sampleFile.html"; stop spamming wikipedia 
r = requests.get(
  'https://en.wikipedia.org/wiki/foo'
)

if r.status_code == 200:
  print ("Got it" + str(r.status_code)) 
  with open("sampleFile.html", "wt") as f:
    f.write(str(r.content)) 


