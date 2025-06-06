#!/home/jku/git/jksfoTemp/python3/flask/env/bin/python

"""
# https://www.youtube.com/watch?v=5aYpkLfkgRE&list=TLPQMDEwMzIwMjXt8nhYePo5FA&index=4
# build a meme Python website (Flask Tutorial for Beginners)

# Make sure pip is current if there are errors
# python -m pip install --upgrade pip setuptools

# Which python installation am I using? (Am I in the venv? )
  # /home/jku/git/jksfoTemp/python3/flask/thisEnv/bin/python

# Activate the virtual environment
source thisEnv/bin/activate
# To return to host ...
# deallocate

# NEED TO CHANGE OWNER OF DIRECTORY
## drwxr-xr-x  5 root root 4096 Mar  1 00:03 thisEnv # THIS WILL CAUSE PERMISSION ERRORS
# sudo chown -R jku:jku ./

# pip install Flask
# pip3 install requests

# To see pip packages in this environment
# pip list

# # For portability, exports the file elements
# pip freeze > requirements.txt (md?)
# # For portability, installs the file elements
# pip install -r requirements.txt

# something else ...

"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # pass
    return "<html><head><title><meta name='viewport' content='width=device-width, initial-scale=1'><meta http-equiv='refresh'content='30;url=http://127.0.0.1:81'><style> body {background-color:#000000;background-repeat:no-repeat;background-position:top-left;}  h1 {text-align:center;font-family:Arial;color:#ffffff;background-color:#000000;}  p {text-align:center;font-family:Georgia; font-size:48px;}</style></head><body><h1> Meme site? </h1><p> here </p><p><img src='{{meme_pic}}'></p><p>Current subreddit: {{subreddit}}</p></body></html>"


app.run(host="0.0.0.0", port=81)
# Using port 81 as apache is running ...

# > * Serving Flask app 'flaskTest'

# * Running on all addresses (0.0.0.0)
# * Running on http://127.0.0.1:81
# * Running on http://10.20.10.83:81

# Make sure that the server is still running when you test it!

