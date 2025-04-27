from . import auth
from flask import render_template

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')