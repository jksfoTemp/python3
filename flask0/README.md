
https://www.browserstack.com/guide/web-development-in-python-guide

jcu@jcu-dev:~$ pip install flask
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

  python3-full

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

# create a virtual environment using
  sudo apt install python3-full
  sudo apt-get install virtualenv

  python3 -m venv path/to/venv.
    python3 -m venv ./flask0/flaskEnv0

Python3 virtualenv error: Operation not permitted - 'lib64'



    python -m ensurepip --default-pip
    source myenv/bin/activate

  sudo pip install flask

