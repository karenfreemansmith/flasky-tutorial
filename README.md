# Building Flasky on Mac OS
This is an app from the "Flask Web Development" book. This read me is detailing the steps for building it on a Mac. (The book has instructions for Linux/Ubuntu and some notes for Windows, but is not always working for me.)

## Virtual Environment
```
python3 -m venv env-name
source env-name/bin/activate
pip install flask
```

## Running Application
* Debug is optional and provides hot reloading
* Runs on localhost:5000 by default
```
export FLASK_APP=hello.py
export FLASK_DEBUG=1
flask run
```
