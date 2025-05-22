
from flask import render_template, url_for
from app import data
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/exercises')
def exercises():
    
    return render_template('exercises.html', title="Exercises", exercises=data.exercises)