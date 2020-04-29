#!/usr/bin/python3
"""Index file"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Return the status"""
    return jsonify({"status": "OK"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def count_classses():
    """Send how many models have in STORAGE"""
    classes = [Amenity, City, Place, Review, State, User]
    show = ["amenities", "cities", "places", "reviews", "states", "users"]

    dict_show = {}

    for clas in range(len(classes)):
        dict_show[show[clas]] = storage.count(classes[clas])

    return jsonify(dict_show)
