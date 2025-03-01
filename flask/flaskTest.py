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
    return "foo"

app.run(host="0.0.0.0", port=81)
# Using port 81 as apache is running ...

# > * Serving Flask app 'flaskTest'

# * Running on all addresses (0.0.0.0)
# * Running on http://127.0.0.1:81
# * Running on http://10.20.10.83:81

# Make sure that the server is still running when you test it!

# https://search.brave.com/search?# q=linux+allow+traffic+on+port+81+for+dev&source=desktop&summary=1&conversation=ed50a560127e1cbc45da2f
# sudo iptables -A INPUT -p tcp --dport 81 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
# sudo iptables-save
# sudo ufw allow 81
# netstat -tapnl | grep :81

