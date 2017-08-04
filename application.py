#!flask/bin/python
from app.app import application

if __name__ == "__main__":
    application.run(debug=True)
