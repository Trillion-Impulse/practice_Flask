from flask import Flask
import random

app = Flask(__name__)

topics = [
    {'id': 1, 'title': 'html', 'body': 'html is...'},
    {'id': 2, 'title': 'css', 'body': 'css is...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is...'}
]

@app.route('/')
def index():
    liTags =''
    for topic in topics:
        liTags = liTags + f'<li><a href={topic["id"]}>{topic["title"]}</a></li>'
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {liTags}
            </ol>
            <h2>Welcome</h2>
            Hello, Web
        </body>
    </html>
    '''

@app.route('/Create/')
def Create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    return 'ID: '+id


app.run(debug=True)