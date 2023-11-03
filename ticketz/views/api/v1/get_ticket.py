from flask import Blueprint, request, flash, redirect, session, jsonify
from ticketz.models import Ticket

view_api_ticket_get = Blueprint('view_api_ticket_get', __name__)

@view_api_ticket_get.get('/get_ticket')
def api_ticket_get():
    if 'id' not in session:
        flash('You must be logged in to access this page.')
        return redirect('/login')
    if not 'code' in request.args:
        return jsonify({'error': True, 'error_message': 'No ticket code provided.'}), 403
    code = request.args.get('code')
    ticket = Ticket.query.filter_by(code=code).first()
    if not ticket:
        return jsonify({'error': True, 'error_message': 'Ticket not found.'}), 403
    return jsonify({'error': False, 'ticket': ticket.to_dict()})