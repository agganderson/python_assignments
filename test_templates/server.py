from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', phrase='Hello', times=10)

@app.route('/sucess')
def success():
	return render_template('success.html')

app.run(debug=True)