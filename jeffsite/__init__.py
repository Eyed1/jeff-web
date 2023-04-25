import os
from flask import (Flask, Blueprint, render_template, session, url_for)
#from . import render_pdf 
app = Flask(__name__, instance_relative_config=True)

def create_app(test_config=None):
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE = os.path.join(app.instance_path, 'jeffblog.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #from . import db
    #db.init_app(app)
    return app

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/writing')
def writing():
    return render_template('writing.html')

#import jeffsite.render_pdf

