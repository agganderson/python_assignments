#for when the user is being put into your database


import md5 #do this at the top of your file where you import modules

@app.route('/users/create', methods=['POST'])
def create_user():
	password = md5.new(request.form['password']).hexdigest();
	email = request.form['email']
	username = request.form['username']
	query = "INSERT INTO users (username, email, password, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(username, email, password)
	mysql.run_my_sql(query)



#for when your user is trying to log into
password = md5.new(request.form['password']).hexdigest()
email = request.form['email']
query = "SELECT * FROM users where users.password = '{}' AND users.email = '{}'".format(email, password);
user = mysql.fetch(query)
#do the neccessary logic to login if the user exists, otherwise redirect to login page with error message


#GENERATING A SALT

import os, binascii #include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15)) #os.urandom() returns a string of bytes with equal to the 
#parameter its given. --> b2a_hex() is a function that will return the value returned from the openssl function
#into a normal alphanumeric

#EX
username = request.form['username']
email = request.form['email']
password = request.form['password']
salt = binascii.b2a_hex(os.random(15))
encrypted_pw = md5.new(password + salt).hexdigest()
query = "INSERT INTO users (username, email, password, salt, created_at, updated_at) VALUES ('{}', '{}', '{}', '{}', NOW(), NOW())".format(username, email, encrypted_pw, salt)
mysql.run_my_sql(query)



## when trying to authenticate a user's login--->
email = request.form['email']
password = request.form['password']
user_query = "SELECT * FROM users WHERE users.email = '{}' LIMIT 1".format(email)
user = mysql.fetch(user_query)
if user[0]:
	encrypted_password = md5.new(password + $user[0]['salt']).hexdigest();
	if $user['password'] == encrypted_password:
		#this means we have a successful login
	else:
		#invalid password
else:
	#invalid email

##USING BCRYPT IN FLASK APP
from flask import Flask, request, render_template
from mysqlconnection import MySQLConnector

#imports the Bcrypt module
from flask.ext.bcrypt import Bcrype
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector('database_name_here')

#this will load a page that has 2 forms, one for registration and  one for login

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


#generate_password_hash--> password has generator that you use when creating new users
@app.route('/create_user', methods=['POST'])
def create_user():
	email = request.form['email']
	username = request.form['username']
	password = request.form['password']
	#run validation and if they are successful we can create the password hash with bcrypt
	pw_has = bcrypt.generate_password_hash(password)
	#how we insert the new user into the database
	insert_query = "INSERT INTO users (email, username, pw_hash, created_at) VALUE ('{}', '{}', '{}', NOW())".format(email, username, pw_hash)
	#redirect to success page



#check_password hash function returns true if the hashed value of password provided at login is equal to the password hash in the database/return false otherwise
password = 'password'
pw_hash = bcrypt.generate_password_hash(password)
test_password_1 = 'thisiswrong'
bcrypt.check_password_hash(pw_hash, test_password_1) #this will return false
test_password_2 = 'password'
bcrypt.check_password_hash(pw_hash, test_password_2) #this will return true



##to use when trying to login might look like this
@app.route('/login', methods=['POSt'])
def login():
	email = request.form['email']
	password = request.form['password']
	user_query = "SELECT * FROM users WHERE email = '{}' LIMIT 1".format(email)
	user = mysql.fetch(user_query) #user will be returned in an array
	if bcrypt.check_password_hash(user[0]['pw_hash'], password):
		#login user
	else:
		#set flash error message and redirect to login page





