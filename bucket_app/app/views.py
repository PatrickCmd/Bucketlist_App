from flask import Flask, request, redirect, render_template, url_for, session
from app import app

# importing class objects
from classes.user import User
from classes.bucketapp import BucketApp

# creating bucketapp object
bucketapp = BucketApp()

#global user object 
current_user  = None

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
    # session['email'] = bucketapp.login(current_user)
    current_user = bucketapp.login(current_user)
    print(current_user)
    # redirect to users bucketlist page
    # return redirect(url_for('bucketlist')) 
    # return render_template('bucketlists.html', user=user)
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
    print(request.form)
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
    return redirect(url_for('login'))
    
@app.route('/bucketlist')
def bucketlist():
    '''users bucketlist template page'''
    # if 'email' not in session:
    #     return redirect(url_for('index'))
    return render_template('bucketlists.html', title='Bucketlists', user=current_user)