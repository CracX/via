from flask import Blueprint, request, flash, redirect, session, render_template
from ticketz.models import Ticket, Admin
from argon2 import PasswordHasher

view_ui_tickets = Blueprint('view_ui_tickets', __name__)

@view_ui_tickets.get('/')
def api_panel_tickets():
    if not 'id' in session:
        flash('You must be logged in to access this page.')
        return redirect('/login')
    admin = Admin.query.filter_by(id=session['id']).first()
    if not admin:
        flash('You must be an admin to access this page.')
        return redirect('/login')
    
    all_tickets = Ticket.query.filter_by().all()
    return render_template('tickets.html', all_tickets=all_tickets)

