# Initialising flask application
from flask import Flask, render_template, redirect

app = Flask(__name__)

app.secret_key = "cmdtelmet@12627*&"

from app import views
