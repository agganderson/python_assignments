from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def result():
	session['name'] = request.form['name']
	session['location'] = request.form['location']
	session['language'] = request.form['language']
	session['comment'] = request.form['comment']
	return redirect('/info')

@app.route('/info')
def info():
	return render_template('process.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])


app.run(debug=True)