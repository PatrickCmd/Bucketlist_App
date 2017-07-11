# Initialising flask application
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return ('Minimal Python Flask application')