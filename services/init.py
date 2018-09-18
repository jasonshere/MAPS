from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import configparser

app = Flask(__name__)
conf = configparser.ConfigParser()
conf.read('config.ini')
env = 'DEVELOPMENT'

USER   = conf.get(env, 'USER')
PASS   = conf.get(env, 'PASS')
HOST   = conf.get(env, 'HOST')
DBNAME = conf.get(env, 'DBNAME')
PREFIX = conf.get(env, 'PREFIX')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(USER,PASS,HOST,DBNAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
