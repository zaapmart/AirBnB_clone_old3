#!/usr/bin/python3
<<<<<<< HEAD
""" Index """
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def number_objects():
    """ Retrieves the number of each objects by type """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenities", "cities", "places", "reviews", "states", "users"]

    num_objs = {}
    for i in range(len(classes)):
        num_objs[names[i]] = storage.count(classes[i])

    return jsonify(num_objs)
=======
"""
Create a Flask app: app_views
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def api_status():
    """
    Returns a JSON response for Restful API health.
    """
    response = {"status" : "OK"}
    return jsonify(response)

@app_views.route('/stats')
def get_stats():
    """

    """
    stats = {
        'amenities': storage.count('Amenity'),
        'cities' : storage.count('City'),
        'places' : storage.count('Place'),
        'reviews': storage.count('Review'),
        'states' : storage.count('State'),
        'users' : storage.count('User'),

    }
    return jsonify(stats)
>>>>>>> 09f3fc3aa0294e193ed76b8c6de9d1056e1c3893
