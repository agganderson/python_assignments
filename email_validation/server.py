from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

app = Flask(__name__)
app.secret_key = 'ThisIsASecret'
mysql = MySQLConnector('mydb')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process ():
	error = 0
	session['email'] = request.form['email']


	if len(request.form['email']) < 1:
		flash('Cannot have empty email field.')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('That was not a valid email address.')
	else:
		error = 1

	if error == 0:
		return redirect('/')

	emails = mysql.fetch("SELECT * FROM emails")
	query = "INSERT INTO emails (address, created_at) VALUES ('{}', NOW()".format(request.form['email'])
	mysql.run_mysql_query(query)

	return redirect('/')

# @app.route('/success')
# def success():

# 	emails = mysql.fetch("SELECT * FROM emails")
# 	return render_template('success.html', emails=emails)


app.run(debug=True)


