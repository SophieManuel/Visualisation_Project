from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)

@app.route('/')
def root():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')
