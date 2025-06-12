
from flask import render_template, url_for, redirect, flash
from app import data
from app import app
from app.forms import LoginForm
from app.models import User
from app import login
from app import db
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/exercises')
def exercises():
    
    return render_template('exercises.html', title="Exercises", exercises=data.exercises)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()

    if form.validate_on_submit():
        query = sa.select(User).where(User.username == form.username.data)
        user = db.session.scalar(query)
        if user is None or not user.check_password(form.password.data):
            flash('Логин или пароль указаны неверно')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

        
        return redirect('/index')
    return render_template('login.html', title='Вход', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))