# janky but it works : bs4-scrape-0.py 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  TODO: See what the output is/was, grab it 
  TODO: Add in main 
  TODO: Add in error checking 
  ODO: Setup error output with filename.err 
  TODO: Check in 
  TODO: fix bs4 reference 
  TODO: switch from http to file reference 
"""

import requests
from bs4 import BeautifulSoup

#soup = BeautifulSoup(html, 'html.parser') 

''' # Get response object; Switch for the file "sampleFile.html"; stop spamming wikipedia 
  # r = requests.get(
  #    'https://en.wikipedia.org/wiki/foo'
  #  )
  # print (r.text) 
  # if r.status_code == 200:
	# soup: bs4.BeautifulSoup = BeautifulSoup(r.content, "html.parser")
'''

# Swapping r (response) obj for f (file) obj 
with open("sampleFile.html") as f:
  # f.write(str (r.content)) 
 	# soup = BeautifulSoup(f.content, "html.parser")
 	soup = BeautifulSoup(f, "html.parser")
  
for someText in soup.find_all("nav", {"class": "vector-toc-landmark"}):
  print(someText.text)

print("See sampleFile.html")


# Work with file ... 
# from bs4 import BeautifulSoup
# 
# with open("C:\\example.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
# 
# for city in soup.find_all('span', {'class' : 'city-sh'}):
#     print(city)

''' # Template file access - write  
  # with open("foo.out.html", "wt") as f:
  #   f.write("This is text!\n")
  #   f.write(headline.text + "\n")        
'''
