from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)

app.secret_key = 'Secret'

@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 0
		session['activities'] = []
	return render_template('index.html', gold=session['gold'], activities=session['activities'])

@app.route('/process_money', methods=['POST'])
def process_money():
	if request.form['building'] == 'farm':
		num = random.randrange(10, 21)
		session['gold'] += num
		sentence = 'You won ' + str(num) + ' from farm!'
		session['activities'].append({'sentence' : sentence, 'status' : 'won'})

	if request.form['building'] == 'cave':
		num = random.randrange(5, 11)
		session['gold'] += num
		sentence = 'You won ' + str(num) + ' from cave!'
		session['activities'].append({'sentence' : sentence, 'status' : 'won'})

	if request.form['building'] == 'house':
		num = random.randrange(2, 6)
		session['gold'] += num
		sentence = 'You won ' + str(num) + ' from house!'
		session['activities'].append({'sentence' : sentence, 'status' : 'won'})

	if request.form['building'] == 'casino':
		num = random.randrange(0, 51)
		takeaway = random.randrange(0, 2)
		if takeaway == 0:
			session['gold'] += num
			sentence = 'You won ' + str(num) + ' from casino'
			session['activities'].append({'sentence' : sentence, 'status' : 'won'})
		else: 
			session['gold'] -= num
			sentence = 'You won ' + str(num) + ' from casino'
			session['activities'].append({'sentence' : sentence, 'status' : 'lost'})

	return redirect('/')

app.run(debug=True)