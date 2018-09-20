from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_session import Session
import configparser
from flask_httpauth import HTTPBasicAuth
import os

app = Flask(__name__)
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

# Database configuration
USER   = conf.get(env, 'USER')
PASS   = conf.get(env, 'PASS')
HOST   = conf.get(env, 'HOST')
DBNAME = conf.get(env, 'DBNAME')
PREFIX = conf.get(env, 'PREFIX')

# HTTP BASE AUTH
auth = HTTPBasicAuth()
APIKEY = conf.get(env, 'APIKEY')
APIPASS = conf.get(env, 'APIPASS')

# DEBUG
DEBUG = conf.get(env, 'DEBUG') == 'true' if True else False

# Initialize Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(USER,PASS,HOST,DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Session config
app.config['SESSION_TYPE'] = conf.get(env, 'SESSION_TYPE')
app.config['SECRET_KEY'] = os.urandom(32)
Session(app)
