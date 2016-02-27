from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if 'random_num' not in session:
		session['random_num'] = random.randrange(1, 101)

	return render_template('index.html') 

@app.route('/result', methods=['POST'])
def guess():

	session['user_num'] = request.form['user_num']

	if int(session['user_num']) == session['random_num']:
		session['message'] = 'congrats'

	elif int(session['user_num']) < session['random_num']:
		session['message'] = 'too low'

	elif int(session['user_num']) > session['random_num']:
		session['message'] = 'too high'
			
	return redirect('/')

@app.route('/success', methods=['POST'])
def success():

	session.clear()

	return redirect('/')

app.run(debug=True)