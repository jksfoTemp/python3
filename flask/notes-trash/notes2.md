
# # Some tips Python3 ...

# # To install virtual environment
# sudo apt install python3.10-venv

# Change directory; here 'abc' is my user
/home/abc/git/abcTemp/python3/

# # Activate the virtual environment
# sudo python3 -m venv thisEnv

# cd to root where the

# !!! Change the ownership of the envinonment
# (thisEnv) abc@abcMain:~/git/jksfoTemp/python3/flask$ ls -la
# drwxr-xr-x  5 root root 4096 Mar  1 00:03 thisEnv
# # sudo chown -R abc:abc ./

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

