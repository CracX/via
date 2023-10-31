from flask import Blueprint, request, flash, redirect, jsonify
from ticketz.models import Admin, db
from argon2 import PasswordHasher

view_api_register = Blueprint('view_api_register', __name__)

@view_api_register.post('/register')
def api_register():
    if not request.form.get('username') or not request.form.get('password') or not request.form.get('email'):
        flash('All fields are required')
        return redirect('/panel/register?error=1')
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')

    check_for_username = Admin.query.filter_by(username=username).first()
    if check_for_username:
        flash('Username already taken')
        return redirect('/panel/register?error=1')
    check_for_email = Admin.query.filter_by(email=email).first()
    if check_for_email:
        flash('Email already taken')
        return redirect('/panel/register?error=1')
    
    admin = Admin(username=username, password_hash=PasswordHasher().hash(password), email=email)
    db.session.add(admin)
    db.session.commit()
    return redirect('/panel/users')



