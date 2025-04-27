from flask import Flask

def create_app():
    app = Flask(__name__)
    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    @app.route('/')
    def main_page():
        return 'HELLO, MAIN PAGE'
    
    return app