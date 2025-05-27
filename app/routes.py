
from flask import render_template, url_for, redirect, flash
from app import data
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/exercises')
def exercises():
    
    return render_template('exercises.html', title="Exercises", exercises=data.exercises)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash("{}".format(form.username.data))
        flash("{}".format(form.username.data))
        return redirect('/index')
    return render_template('login.html', title='Вход', form=form)
