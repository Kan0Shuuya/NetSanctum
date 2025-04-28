from flask import Blueprint

bp = Blueprint("clnd", __name__, template_folder='templates')

from . import routes