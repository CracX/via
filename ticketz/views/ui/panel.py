from flask import Blueprint, flash, redirect, session, render_template
from ticketz.models import Admin

view_ui_panel = Blueprint('view_ui_panel', __name__)

@view_ui_panel.route('/')
def api_panel():
    if not 'id' in session:
        flash('You must be logged in to access this page.')
        print('here')
        return redirect('/login')
    
    admin = Admin.query.filter_by(id=session['id']).first()
    if not admin:
        flash('You must be logged in to access this page.')
        print('here2')
        return redirect('/login')
    
    return render_template('panel.html', admin=admin)
