from flask import Blueprint

bp = Blueprint("notes_bp", __name__, template_folder='templates')

from . import routes