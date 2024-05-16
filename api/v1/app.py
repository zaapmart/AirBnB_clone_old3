#!/usr/bin/python3
"""
Create a Flask app: app_views and register the blueprint
"""
from os import getenv
from flask import Flask
from api.v1.views import app_views
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)

if __name__ == '__main__':
    Host = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=Host, port=PORT, threaded=True)
