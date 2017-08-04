#!flask/bin/python
from flask import Flask

application = app = Flask(__name__)
from app import views

application.run(debug=True)
