from flask import Blueprint, render_template

view_ui_index = Blueprint('view_ui_index', __name__, template_folder='templates')

@view_ui_index.route('/')
def view_index():
    return render_template('index.html')