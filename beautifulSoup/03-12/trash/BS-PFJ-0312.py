#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random
import re
# import sys
import time


import bs4
# import numpy as np
import pandas as pd
# import requests
from bs4 import BeautifulSoup


# def delay() -> None:
#     time.sleep(random.uniform(15, 30))
#     return None

# switch to file reference 
# https://www.postjobfree.com/jobs?q=%22data+entry%22&n=&t=&c=&l=San+Francisco%2C+CA&radius=2&r=100 

# wget -O pfj-DE-100-0312.html https://www.postjobfree.com/jobs?q=%22data+entry%22&n=&t=&c=&l=San+Francisco%2C+CA&radius=2&r=100

# base: str = "https://www.sequoiacap.com/companies/"

content: dict = {
    "name": [],
    "url": [],
    "description": [],
    "milestones": [],
    "team": [],
    "partner": []
}

# delay()
# r: requests.Response = requests.get(base)
# soup: bs4.BeautifulSoup = BeautifulSoup(r.content, "html.parser")

with open("/home/jku/git/jksfoTemp/python3/beautifulSoup/03-12/pfj-DE-100-0312-1.html") as f:
#          pfj-DE-100-0312-1.html
  # f.write(str (r.content)) 
 	# soup = BeautifulSoup(f.content, "html.parser")
 	soup = BeautifulSoup(f, "html.parser")
    
# pfj-DE-100-0312-1.html

for someText in soup.find_all("div", {"class": "normalText"}):
  print(someText.text)


# Write scraped data to disk.
df: pd.DataFrame = pd.DataFrame(content)
df = df.replace("", np.nan).fillna(value="NA")
df.to_csv("../01_data/requests_output.csv",
          index=False,
          sep=";",
          encoding="utf-8")
          

print("See sampleFile.html")
