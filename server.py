from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome'

@app.route('/Create/')
def Create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    return 'ID: '+id


app.run(debug=True)