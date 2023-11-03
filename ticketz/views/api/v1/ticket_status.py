from flask import Blueprint, request, flash, redirect, session
from ticketz.models import Ticket, Admin, db
from ticketz.ext.enums import TicketStatus

view_api_ticket_status = Blueprint('view_api_ticket_status', __name__)

@view_api_ticket_status.get('/')
def api_panel_ticket_status():
    if not 'id' in session:
        flash('You must be logged in to access this page.')
        return redirect('/login')
    admin = Admin.query.filter_by(id=session['id']).first()
    if not admin:
        flash('You must be an admin to access this page.')
        return redirect('/login')
    
    if not request.args.get('code') or not request.args.get('status'):
        flash('You must specify an id and status.')
        return redirect('/tickets')
    
    ticket = Ticket.query.filter_by(code=request.args.get('code')).first()
    if not ticket:
        flash('Ticket not found.')
        return redirect('/tickets')
    
    try:
        status = int(request.args.get('status'))
    except ValueError:
        flash('Status must be an integer.')
        return redirect('/tickets')
    if status == 1:
        status = TicketStatus.IN_PROGRESS
    elif status == 2:
        status = TicketStatus.CLOSED
    else:
        flash('Status must be 1 or 2.')
        return redirect('/tickets')
    
    ticket.status = status
    db.session.commit()
    return redirect('/tickets')
    

