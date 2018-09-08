# import necessary packages
from flask import Flask, render_template, session, redirect, url_for, request, jsonify
from flask_bootstrap import Bootstrap
import os

# Initialize framework
app = Flask(__name__)
Bootstrap(app)

# create secret key for form to avoid CSRF attack
app.secret_key = os.urandom(32)

# root
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)