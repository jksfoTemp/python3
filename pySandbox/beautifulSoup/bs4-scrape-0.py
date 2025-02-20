# janky but it works : bs4-scrape-0.py 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# TODO: Check in 
# TODO: Why does this editory keep crashing whenever I do a save-as and try to copy the file name? 
# TODO: Add in main 
# TODO: Add in error checking 
# TODO: See what the output is/was, grab it 
# TODO: Setup error output with filename.err 
# TODO: Check in 
# TODO: fix bs4 reference 


import requests
from bs4 import BeautifulSoup

#soup = BeautifulSoup(html, 'html.parser') 

r = requests.get(
  # 'https://en.wikipedia.org/wiki/Web_scraping'
  'https://en.wikipedia.org/wiki/foo'
  )

print (r.status_code) #  == 200

# print (r.text) #  == 200

if r.status_code == 200:
	# soup: bs4.BeautifulSoup = BeautifulSoup(r.content, "html.parser")
 	soup = BeautifulSoup(r.content, "html.parser")
  # for headline in soup.find_all("span", {"class": "mw-headline"}):
for headline in soup.find_all("nav", {"class": "vector-toc-landmark"}):
  print(headline.text)
  print("foo.out.html")
  # print(headline.text) 
  # foo.out.html

# Work with file ... 
# from bs4 import BeautifulSoup
# 
# with open("C:\\example.html") as fp:
#     soup = BeautifulSoup(fp, 'html.parser')
# 
# for city in soup.find_all('span', {'class' : 'city-sh'}):
#     print(city)


with open("foo.out.html", "wt") as f:
  f.write("This is text!\n")
  f.write(headline.text + "\n")        
