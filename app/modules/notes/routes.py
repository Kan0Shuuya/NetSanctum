from . import bp
from flask import current_app, render_template

@bp.route("/")
def main():
    modules=current_app.config.get('MODULES', [])
    module=next((m for m in modules if m['name'] == 'Заметки'), None)
    return render_template("index.html", modules=modules, module=module)
    