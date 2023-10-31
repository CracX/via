from flask import Blueprint

view_ui_index = Blueprint('view_ui_index', __name__, template_folder='templates')

@view_ui_index.route('/')
def view_index():
    return 'Hello World!'