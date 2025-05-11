#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import re
import sys
import time

# import bs4\


# import requests
from bs4 import BeautifulSoup

# content: dict = {
#     "name": [],
#     "url": [],
#     "description": [],
#     "milestones": [],
#     "team": [],
#     "partner": [],
# }

with open(
    "/home/jku/git/jksfoTemp/python3/beautifulSoup/03-12/pfj-DE-100-0312-5a.html"
) as f:
    # pfj-DE-100-0312-5.html
    soup = BeautifulSoup(f, "html.parser")
    with open("output.html", "w", encoding="utf-8") as file:

        for someText in soup.find_all("span", {"class": "colorCompany"}):
            print(someText.text)

            # Writing the content to an HTML file with prettify
            # with open("output.html", "w", encoding="utf-8") as file:
            # file.write(soup.prettify())
            # file.write(soup.prettify(someText.text))
            file.write(someText.text + "\n")


# # Write scraped data to disk.
# df: pd.DataFrame = pd.DataFrame(content)
# df = df.replace("", np.nan).fillna(value="NA")
# df.to_csv("../01_data/requests_output.csv",
#           index=False,
#           sep=";",
#           encoding="utf-8")


# print("See sampleFile.html")
