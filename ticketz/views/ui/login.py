from flask import Blueprint, render_template

view_ui_login = Blueprint('view_ui_login', __name__, template_folder='templates')

@view_ui_login.get('/')
def view_login():
    return render_template('login.html')
