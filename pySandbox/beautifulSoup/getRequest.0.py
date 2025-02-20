#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Only using this to download a save a sample page 
  getRequest.0.py 'foo.com' 'foo.txt' 
    # def main(url='', outputFile='', verbose=False):
      # url = 'https://en.wikipedia.org/wiki/foo' 
      # outputFile = 'sampleFile.html' 
  Output file: sampleFile.html
  
  TODO: Parse with PyLance (remove other linters)
  TODO: Implement variable typing
  TODO: Set up a decent formatter that actually works (unlike black)
  TODO: Implement logging 

'''

import requests
import os 
import sys 

# Removed - was just being used for testing 
# class Stubb(object):
#   def __init__(self, status_code, content):
#     self._status_code = status_code
#     self._content = content

#   def name(self):
#     return self._status_code, self._content


def getURLObj(urlT): 
  try: 
    # REMOVEME
    # r = stubb (200, "foo")
    # print (r.status_code)
    # print (r.content)
    
    r = requests.get(
         urlT 
    )
    if r.status_code == 200:
      print ("Got it: {r.status_code}")
      return r.content
    else: 
      print ("Error getting url: {urlT}  Response status code: \
        {r.status_code)}") 
      return None 

  except requests.exception.RequestException as e: 
    print ("Error getting url: {urlT};  Response status code: \
      {r.status_code}") 
    return None 


def writeObj(obj, outFile): 
  if obj is None: # Handle case where no content was retrieved
    print(f"No content to write to file: {obj} \n {outFile}")
    return

  try: 
    with open(outFile, "wt") as f:
      # f.write(str(obj.content)) # bad 
      f.write(obj.decode('utf-8')) # Decode bytes to string before writing 
    
  except Exception as e:
    print(f"An error occurred writing the file: {e}")


# def main(url='https://en.wikipedia.org/wiki/foo', 
#  outputFile='sampleFile.html', verbose=False):
def main( \
  url="https://en.wikipedia.org/wiki/foo", \
    outputFile="sampleFile.html", \
      verbose=False):
  try:   
    obj = getURLObj(url) # verbose 
    if obj: # Only write if content was successfully retrieved
      writeObj(obj, outputFile)
      print ("Should be good. \n \t URL: {url} \
        \t File: {outputFile} \
          \t Output: {verbose}")
      return_status = 0 
    else: 
      print ('Failed to retrieve content from URL.')
      return_status = -1 
  except Exception as e:
    print(f"An error occurred in main: {e}")
    return_status = 1
  finally:
    sys.exit(return_status) # Exit with the determined status code


if __name__ == "__main__": \
  # bad syntax (list of arguments instead of individual arguments)
  # main(sys.argv[0], sys.argv[1], sys.argv[2]) 
  if len(sys.argv) == 4: # Check for correct number of arguments
    url_arg = sys.argv[1]
    output_file_arg = sys.argv[2]
    verbose_arg = sys.argv[3]
    main(url_arg, output_file_arg, verbose_arg)
  elif len(sys.argv) == 3: 
    url_arg = sys.argv[1]
    output_file_arg = sys.argv[2]
    main(url_arg, output_file_arg)
  elif len(sys.argv) == 2: # Allow URL only, use default output file
    url_arg = sys.argv[1]
    main(url_arg)
  elif len(sys.argv) == 1: # Allow URL only, use default output file
    main(url_arg)
  else:
    print("Usage: getRequest.0.py 'URL_to_download' 'output_file.html' \
       [TRUE/FALSE] \
        (\t getRequest.0.py {sys.argv[1]}, {sys.argv[2]}, {sys.argv[3]})")
    print("       getRequest.0.py 'URL_to_download' \
      (\t getRequest.0.py {sys.argv[1]}, {sys.argv[2]})")
    print("       getRequest.0.py 'URL_to_download' \
      (\t getRequest.0.py {sys.argv[1]})")
    print("       getRequest.0.py \
      (\t getRequest.0.py)")
    print("Error: Incorrect number of arguments.")

