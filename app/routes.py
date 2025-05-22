
from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/exercises')
def exercises():
    exercises = [
        {
            "name": "Отжимания от пола",
            "muscle_groups": [ "грудь", "трицепцы"],
            "equipment": ["пол", "кроссовки"]
        },
        {
            "name": "Приседания со штангой",
            "muscle_groups": [ "квадрицепцы", "спина"],
            "equipment": ["штанга"]
        }
    ]
    return render_template('exercises.html', title="Exercises", exercises=exercises)