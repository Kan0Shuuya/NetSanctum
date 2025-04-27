import os
from flask import Flask, abort, redirect, render_template, current_app, request, session, url_for
import config
import auth.routes

def create_app():
    app = Flask(__name__)
    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.config.from_object(config.Config)
    
    @app.route('/')
    @auth.routes.my_login_required()
    def index():
       return render_template('workspace.html', user=session['user'])
        
    return app