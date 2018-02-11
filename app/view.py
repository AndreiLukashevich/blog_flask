from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'Andrei'
    return render_template('index.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('security/404.html'), 404


