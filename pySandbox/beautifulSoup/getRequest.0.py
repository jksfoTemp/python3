#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Only using this to download a save a sample page 
  getRequest.0.py 'foo.com' 'foo.txt' 
    # def main(url='', outputFile='', write_to_stdout=False):
      # url = 'https://en.wikipedia.org/wiki/foo' 
      # outputFile = 'sampleFile.html'
  Output file: sampleFile.html
  TODO: Add logging 
  TODO: Add exception types 
"""

import requests
import os 
import sys 

class Stubb(object):
  def __init__(self, status_code, content):
    self._status_code = status_code
    self._content = content

  def name(self):
    return self._status_code, self._content

def getURLObj(urlT): 
  try: 
    r = stubb (200, "foo")
    print (r.status_code)
    print (r.content)
    
    # STUBBED OUT FOR TESTING 
    # r = requests.get(
    #   urlT 
    # )
    if r.status_code == 200:
      # print ("Got it" + str(r.status_code)) # error? 
      print ( str(r.status_code)) 
      return r.content
    else: 
      print ("Error getting url: " + urlT + " Response status code: " ) # + str(r.status_code)) 

  except Exception as e: 
      print ("Error getting url: " + urlT + " Response status code: " ) # + str(r.status_code)) 

def writeObj(obj, outFile): 
  try: 
    with open(outFile, "wt") as f:
      f.write(str(obj.content)) 
    
    #huh = open(outFile, "wt") 
    #with huh: 
    #  huh.write(str(obj.content)) 

  except Exception as e:
    print(f"An error occurred writing the file: {e}")

def main(url='https://en.wikipedia.org/wiki/foo', outputFile='sampleFile.html', write_to_stdout=False):
  try:   
    obj = getURLObj(url) # write_to_stdout 
    writeObj(obj, outputFile)
    print ('Should be good: ' + outputFile)

  except Exception as e:
      print(f"An error occurred in main: {e}")

if __name__ == "__main__":
  # main(sys.argv[0], sys.argv[1], sys.argv[2])
  main(sys.argv[0:], sys.argv[1:], sys.argv[2:])
  