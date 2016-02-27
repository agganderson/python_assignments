from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():

	return render_template('index.html')

@app.route('/process', methods=['POST'])
def result():
	error = 0
	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comment'] = request.form['comment']


	if len(request.form['name']) < 1:
		flash('Name field cannot be empty!') 
	elif len(request.form['comment']) < 1:
		flash('Comment field cannot be empty!')
	elif len(request.form['comment']) > 120:
		flash('Comment field is too full!')
	else:
		error = 1

	if error == 0:
		return redirect('/')

	return redirect('/info')


@app.route('/info')
def info():

	return render_template('process.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])


app.run(debug=True)