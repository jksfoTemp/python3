#!/home/jku/git/jksfoTemp/python3/flask/env/bin/python

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    #Uncomment these two lines and comment out the other url line
    # url = "https://meme-api.herukoapp.com/gimme"
    url = "https://www.reddit.com/"

    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    return render_template("meme_index.html", meme_pic=mem_pic, subreddit=subreddit)

# app.run (host="0.0.0.0", port=5000)
app.run (host="0.0.0.0", port=81)

# 45.79.2.29:80
