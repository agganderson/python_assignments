from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index(): 
	return render_template('index.html')

@app.route('/ninjas')
def ninja():
	return render_template('ninjas.html')

@app.route('/dojos')
def dojo():
	return render_template('dojos.html')

@app.route('/dojos/new')
def new():
	return render_template('new.html')

app.run(debug=True)