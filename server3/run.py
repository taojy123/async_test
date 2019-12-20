from flask import Flask, escape, request
import requests
import time


app = Flask(__name__)

@app.route('/')
def hello():
    url = 'http://lovegaudi.art:3000'
    requests.get(url)
    return 'Hello'


# pip3 install flask gevent
# 
# FLASK_APP=run.py flask run -h 0.0.0.0
# or
# gunicorn run:app -b 0.0.0.0:5000 -k gevent

