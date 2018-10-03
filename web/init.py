from flask import Flask, request, jsonify, session
from flask_bootstrap import Bootstrap

import configparser
import os

app = Flask(__name__)
Bootstrap(app)
# create secret key for form to avoid CSRF attack
app.secret_key = os.urandom(32)

conf = configparser.ConfigParser()
conf.read('config.ini')
# MAIN
environment = conf.get('MAIN', 'ENVIRONMENT')

# Identify development environment
if environment == 'dev':
    env = 'DEVELOPMENT'
elif environment == 'pro':
    env = 'PRODUCTION'

# HTTP BASE AUTH
SERVICE_ADDRESS = conf.get(env, 'SERVICE_ADDRESS')
PROTOCOL = conf.get(env, 'PROTOCOL')
APIKEY = conf.get(env, 'APIKEY')
APIPASS = conf.get(env, 'APIPASS')

# DEBUG and PORT
DEBUG = conf.get(env, 'DEBUG') == 'true' if True else False
PORT = conf.get(env, 'PORT')
