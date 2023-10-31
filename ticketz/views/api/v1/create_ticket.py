from flask import Blueprint, request, flash, redirect, jsonify
from ticketz.models import Device, Ticket, db
from argon2 import PasswordHasher
import uuid

view_api_ticket_create = Blueprint('view_api_ticket_create', __name__)

@view_api_ticket_create.post('/register')
def api_ticket_create():
    if not request.form.get('code') or not request.form.get('description'):
        flash('All fields are required')
        return redirect('/submit?error=1')
    code = request.form.get('code')
    description = request.form.get('description')

    device = Device.query.filter_by(code=code).first()
    if not device:
        flash('Device not found')
        return redirect('/submit?error=1')
    random_code = ""
    while True:
        random_code = str(uuid.uuid4())
        if not Ticket.query.filter_by(code=random_code).first():
            break
    ticket = Ticket(device_id=device.id, code=random_code, description=description)
    db.session.add(ticket)
    db.session.commit()
    return redirect('/check?code=' + random_code)


