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
  

  '''
AI suggestions ... 

Here's a breakdown of the problems and the fixes:
  
Problems and Solutions:

Stubbed requests.get:

Problem: The actual HTTP request was commented out and replaced with a stub, preventing real webpage downloads.
Solution: Uncommented r = requests.get(urlT) and removed the Stubb class and stub instantiation. Now the script makes actual HTTP requests.
Incorrect Stubb class and usage:

Problem: Stubb class was unnecessary for the script's stated purpose and was misleading.
Solution: Removed the Stubb class entirely as it was only hindering the script's functionality for downloading pages.
Error message in getURLObj incomplete:

Problem: Error messages were missing the actual status code from the response.
Solution: Modified the error message in getURLObj to use f-strings and include r.status_code when available. Also changed the except to catch requests.exceptions.RequestException for more specific handling of request-related errors and included the exception e in the error message for debugging.
Incorrect command-line argument handling in main call:

Problem: main(sys.argv[0:], sys.argv[1:], sys.argv[2:]) was passing lists of arguments instead of individual arguments, and slicing sys.argv incorrectly.
Solution: Corrected the if __name__ == "__main__": block to properly handle command-line arguments.
Added checks for the number of arguments (len(sys.argv)).
If 3 arguments (script name, URL, output file), it now correctly extracts sys.argv[1] as URL and sys.argv[2] as output file.
If 2 arguments (script name, URL only), it uses the provided URL and the default outputFile='sampleFile.html'.
If incorrect number of arguments, prints usage instructions.
write_to_stdout argument not used:

Problem: The write_to_stdout argument in main was defined but not used.
Solution: Removed write_to_stdout from the main function signature to simplify the script, as it was not implemented. If this functionality is needed, it would require adding logic to main and writeObj to handle writing to standard output.
Leftover "s code?" and Stubb class:

Problem: Irrelevant text and unnecessary class.
Solution: Removed "s code?" and the Stubb class.
Decoding content before writing:

Problem: r.content returns bytes. Writing bytes directly to a text file might cause encoding issues.
Solution: In writeObj, added .decode('utf-8') to obj.content before writing to decode the bytes content to a UTF-8 string, which is a common encoding for web pages and text files.
Handling None content:

Problem: If getURLObj fails to get content (non-200 status or exception), it could potentially pass None to writeObj, leading to an error if writeObj expects an object with a .content attribute.
Solution:
getURLObj now returns None in case of errors.
writeObj now checks if obj is None at the beginning. If it is, it prints a message and returns without writing, preventing errors and informing the user if no content was retrieved.
main now checks if obj from getURLObj is not None before calling writeObj, ensuring writeObj is only called with valid content.
Improved Usage Instructions:

Problem: The usage instructions were basic.
Solution: Updated the docstring and the usage instructions printed when arguments are incorrect to be more clear, including examples of how to run the script with both URL and output file, or just URL.
Now the script should correctly download webpages and save them to files, handle basic errors, and provide better command-line argument handling and usage instructions. It is still basic and lacks features like logging, more specific exception handling (TODOs from original script), but it addresses the immediate problems in the provided code.
  '''