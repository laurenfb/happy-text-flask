from flask import Flask

application = Flask(__name__)

from flask import render_template


@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html',)

@application.route('/success')
def success():
    return render_template('success.html',)
