from . import bp
from flask import render_template

@bp.route("/")
def main():
    return "CALENDAR"