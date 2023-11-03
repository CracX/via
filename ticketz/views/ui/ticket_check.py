from flask import Blueprint, render_template, request, flash
from ticketz.models import Ticket
from ticketz.ext.enums import TicketStatus

view_ui_ticket_check = Blueprint('view_ui_ticket_check', __name__, template_folder='templates')

@view_ui_ticket_check.route('/')
def view_ticket_check():
    if not request.args.get('code'):
        return render_template('ticket-check.html')
    
    ticket = Ticket.query.filter(Ticket.code == request.args.get('code')).first()
    if not ticket:
        flash('Invalid code')
        return render_template('ticket-check.html')
    
    if ticket.status == TicketStatus.OPEN:
        status = "OPEN"
    elif ticket.status == TicketStatus.IN_PROGRESS:
        status = "IN PROGRESS"
    else:
        status = "CLOSED"
    
    return render_template('ticket-check.html', status=status)

    