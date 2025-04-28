from flask import Blueprint

bp = Blueprint("clnd", __name__, template_folder='.')

from . import routes