

sudo apt install python3.10-venv

# activate the virtual environment
sudo python3 -m venv thisEnv

# !!! Change the ownership of the envinonment
# (thisEnv) jku@jkMain:~/git/jksfoTemp/python3/flask$ ls -la
# drwxr-xr-x  5 root root 4096 Mar  1 00:03 thisEnv
# # sudo chown -R jku:jku ./

# source env/bin/activate
  # will see (env) in front of prompt
  # source env/bin/
# deactivate

pip list

pip3 install requests
pip3 install flask

# # For portability, exports the file elements
# pip freeze > requirements.txt (md?)
# # For portability, installs the file elements
# pip install -r requirements.txt

