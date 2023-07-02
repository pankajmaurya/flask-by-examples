# myblueprint.py

from flask import Blueprint

my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/blueprint')
def blueprint_route():
    return 'This is a route from the blueprint!'
