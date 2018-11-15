from flask import Blueprint

AppBp = Blueprint('AppBp', __name__)

from . import user, errors