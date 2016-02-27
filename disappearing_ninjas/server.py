from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'Secret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/ninja')
def ninja():
	return render_template('ninjas.html')

# @app.route('/ninja/<blue>')
# def ninjacolor(blue):
# 	return render_template('ninjas.html', blue=blue)



app.run(debug=True)