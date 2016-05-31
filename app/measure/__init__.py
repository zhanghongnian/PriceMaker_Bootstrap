from flask import Blueprint

measure = Blueprint('measure', __name__)

from . import views