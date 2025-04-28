import importlib
import json
import os
from flask import Flask, abort, redirect, render_template, current_app, request, session, url_for


def create_app():
    app = Flask(__name__)
    module_list = []
    modules_dir = os.path.join(os.path.dirname(__file__), 'modules')
    for module_folder in os.listdir(modules_dir):
        full_path = os.path.join(modules_dir, module_folder)
        if os.path.isdir(full_path):
            info_json = os.path.join(full_path, "info.json")
            if os.path.exists(info_json):
                print("Import {info_json}...")
                with open(info_json, encoding="utf-8") as file:
                    meta = json.load(file)
                    py_mod = importlib.import_module(f"app.modules.{module_folder}")
                    if hasattr(py_mod, 'bp'):
                        app.register_blueprint(py_mod.bp, url_prefix=meta.get('route_prefix'))
                        module_list.append({
                            "emoji": f"{meta.get('emoji')}",
                            "name": f"{meta.get('name')}",
                            "href": f"{meta.get('route_prefix')}"
                        })
                    else:
                        print("EROR! not found bp attr in module!")                    
            else:
                print(f"EROR! can't export {info_json}")        
        else:
            print(f"EROR! {full_path} is not dir")   
        app.config['MODULES'] = module_list         
            
    
    
    @app.route('/')
    def index():
       return render_template('workspace.html', modules=current_app.config.get('MODULES', []))
        
    return app