from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from ticketz.ext.enums import TicketStatus
db = SQLAlchemy()

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    code = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Enum(TicketStatus), nullable=False, default=TicketStatus.OPEN)

    device = db.relationship('Device', backref=db.backref('tickets', lazy='dynamic'))