from flask import Blueprint

make_order = Blueprint('make_order', __name__)

from . import views