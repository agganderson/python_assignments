from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if 'random_num' not in session:
		session['random_num'] = random_randrandom(1, 101)	
	return render_template('index.html')

@app.route('/')



app.run(debug=True)