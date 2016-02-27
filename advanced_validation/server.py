from flask import Flask, session, redirect, request, render_template, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
	session['email'] = request.form['email']
	if len(request.form['email']) < 1:
		flash('Email field cannot be blank!')
	#modify the validation conditional to include a case for an invalid email
	elif not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email address')
	else:
		flash('Success')

	return redirect('/')

app.run(debug=True)