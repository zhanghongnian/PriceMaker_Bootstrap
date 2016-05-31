from flask import Blueprint

part_type = Blueprint('part_type', __name__)

from . import views