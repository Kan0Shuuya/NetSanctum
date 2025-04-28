from . import bp
from flask import current_app, render_template

@bp.route("/")
def main():
    return render_template("index.html", modules=current_app.config.get('MODULES', []))