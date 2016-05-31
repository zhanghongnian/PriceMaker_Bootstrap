from flask import Blueprint

part = Blueprint('part', __name__)

from . import views