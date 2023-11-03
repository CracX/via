from flask import Blueprint, request, flash, redirect, session
from ticketz.models import Admin
from argon2 import PasswordHasher

view_api_logout = Blueprint('view_api_logout', __name__)

@view_api_logout.get('/')
def api_logout():
    session.clear()
    return redirect('/')

