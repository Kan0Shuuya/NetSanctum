from flask import Blueprint

bp = Blueprint("cldr", __name__, template_folder='templates')

from . import routes