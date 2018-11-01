"""
Example python app with the Flask framework: http://flask.pocoo.org/
"""

from os import environ

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def index():
    return "JR is learning!!"

@app.route('/jay')
def name():
    return "Hey jay"    

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)