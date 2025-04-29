import os
from . import bp
from flask import current_app, render_template

def folder_to_json(path):
    def scan_dir(cur_path):
        result = {
            'files-in-dir': [f for f in os.listdir(cur_path) if os.path.isfile(os.path.join(cur_path, f))],
            'folders': {}
        }
        for name in os.listdir(cur_path):
            sub_path = os.path.join(cur_path, name)
            if os.path.isdir(sub_path):
                result['folders'][name] = scan_dir(sub_path)
        return result

    abs_path = os.path.abspath(path)
    base_name = '.'
    return {base_name: scan_dir(abs_path)}


@bp.route("/")
def main():
    modules=current_app.config.get('MODULES', [])
    module=next((m for m in modules if m['name'] == 'Заметки'), None)
    print(os.path.normpath)
    return render_template("index.html", modules=modules, module=module, folders=folder_to_json("./app/modules/notes/folder"))
    