from flask import Blueprint, render_template

view_ui_ticket_submit = Blueprint('view_ui_ticket_submit', __name__, template_folder='templates')

@view_ui_ticket_submit.route('/')
def view_ticket_submit():
    return render_template('ticket-submit.html')