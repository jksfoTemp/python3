"""_summary_
  Tutorial: _https://code.visualstudio.com/docs/python/tutorial-flask
"""

import re
from datetime import datetime

from flask import Flask
from flask import request
from flask import render_template

App = Flask(__name__)

# out of scope? # here = str(request.url)

# contents redistributed per refactor step 7


# TODO: Try/catch
@App.route("/")  # http://localhost:5081/c
def home():
    # here: str = str(request.url)
    here = str(request.url)
    # return "Hello, Flask is empty again!" + here
    return render_template("home.html")


# New functions
@App.route("/about/")
def about():
    return render_template("about.html")


@App.route("/contact/")
def contact():
    return render_template("contact.html")


@App.route("/hello/<name>")  # http://localhost:5081/hello/foo
def hello_there(name=None):
    return render_template("hello.html", name=name, date=datetime.now())


@App.route("/api/data")
def get_data():
    return App.send_static_file("data.json")


"""
# layout moved to html template 
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    # print (str(request.url))
    here = str(request.url)
    return content + here
"""
