from flask import Blueprint, request, flash, redirect, session
from ticketz.models import Admin
from argon2 import PasswordHasher

view_api_login = Blueprint('view_api_login', __name__)

@view_api_login.post('/login')
def api_login():
    if not request.form.get('username') or not request.form.get('password'):
        flash('Username and password are required')
        return redirect('/login?error=1')
    
    username = request.form.get('username')
    password = request.form.get('password')

    admin = Admin.query.filter_by(username=username).first()
    if not admin:
        flash('Invalid username or password')
        return redirect('/login?error=1')
    
    try:
        PasswordHasher().verify(admin.password_hash, password)
    except:
        flash('Invalid username or password')
        return redirect('/login?error=1')
    session['id'] = admin.id
    session['username'] = admin.username
    return redirect('/panel')

