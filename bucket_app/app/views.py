from flask import Flask, request, redirect, render_template, url_for, session, flash
from app import app

# importing class objects
from classes.user import User
from classes.bucketapp import BucketApp
from classes.bucketlist import Bucket

# creating bucketapp object
bucketapp = BucketApp()

#global user objects
current_user  = None
user_bucket   = None

@app.route('/')
@app.route('/index')
def index():
    '''Render index page'''
    # return ('Minimal Python Flask application')
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Render login template to login user'''
    if request.method == 'GET':
        return render_template('login.html', title='Login')

    # getting login form variables
    email = request.form['email']
    password = request.form['password']
    # creating object for logged in user
    global current_user 
    current_user = User(email, password)
    current_user = bucketapp.login(current_user)
    return redirect(url_for('bucketlist'))

@app.route('/logout')
def logout():
    '''logging out a user'''
    session.pop('email', None)
    return redirect(url_for('index'))

@app.route('/create', methods=['GET', 'POST'])
def create():
    '''Renders register template for creating user'''
    if request.method == 'GET':
        return render_template('register.html', title='Register')

    # getting form variables
    firstname = request.form['firstname']
    lastname  = request.form['lastname']
    username  = request.form['username']
    email     = request.form['email']
    password  = request.form['password']

    # creating the user account from the user object
    global current_user
    current_user = User(email, password, firstname, lastname, username)
    
    # Append user object to a list of already created users
    bucketapp.registerUser(current_user)
    print(current_user)
    flash("You have successfully created your account please proceed to login")
    return redirect(url_for('login'))
    
@app.route('/bucketlist')
def bucketlist():
    '''users bucketlist template page'''
    return render_template('bucketlists.html', title='Bucketlists', user=current_user)

@app.route('/create_bucket', methods=['POST'])
def create_bucket():
    '''view to create user buckets'''
    bucket_name = request.form['name']
    description = request.form['description']
    print(request.form)
    # creating bucket object for the current user
    global user_bucket
    user_bucket = Bucket(bucket_name, description)
    print(user_bucket)
    # adding bucket to user's bucketlist
    global current_user
    current_user.create_user_bucketlist(user_bucket)
    return redirect(url_for('bucketlist'))
