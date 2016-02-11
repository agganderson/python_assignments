from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app.secret_key = 'ASecret'

@app.route('/')
def index():

	return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
	error = 0
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['email'] = request.form['email']
	session['password'] = request.form['password']
	session['confirm_password'] = request.form['confirm_password']



	if len(request.form['first_name']) < 1: 
		flash('Please enter your First Name!')
	elif not request.form['first_name'].isalpha():
		flash('You cannot have numbers in your name')
	elif len(request.form['last_name']) < 1:
		flash('Please enter your Last Name!')
	elif not request.form['last_name'].isalpha():
		flash('You cannot have numbers in your name')

	elif len(request.form['email']) < 1:
		flash('Please enter an email!')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Your email is not valid')

	elif len(request.form['password']) < 1:
		flash('You need to enter a password..')
	elif len(request.form['password']) < 8:
		flash('You need a longer password')

	elif len(request.form['confirm_password']) < 1:
		flash('You need to confim your password')
	elif request.form['confirm_password'] != request.form['password']:
		flash('Your passwords do not match')

	else:
		error = 1

	if error == 0:
		return redirect('/')

	return redirect('/success')

@app.route('/success')
def success():

	return render_template('success.html')

app.run(debug=True)