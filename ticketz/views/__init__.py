from ticketz.views.ui.index import view_ui_index
from ticketz.views.ui.login import view_ui_login
from ticketz.views.ui.panel import view_ui_panel
from ticketz.views.ui.tickets import view_ui_tickets
from ticketz.views.ui.ticket_submit import view_ui_ticket_submit
from ticketz.views.api.v1.login import view_api_login
from ticketz.views.api.v1.logout import view_api_logout
from ticketz.views.api.v1.register import view_api_register
from ticketz.views.api.v1.create_ticket import view_api_ticket_create
from ticketz.views.api.v1.get_ticket import view_api_ticket_get
from ticketz.views.api.v1.ticket_status import view_api_ticket_status

def build_views(app):
    app.register_blueprint(view_ui_index, url_prefix='/')
    app.register_blueprint(view_ui_login, url_prefix='/login')
    app.register_blueprint(view_api_logout, url_prefix='/logout')
    app.register_blueprint(view_ui_panel, url_prefix='/panel')
    app.register_blueprint(view_ui_tickets, url_prefix='/panel/tickets')
    app.register_blueprint(view_ui_ticket_submit, url_prefix='/submit')
    app.register_blueprint(view_api_login, url_prefix='/api/v1')
    app.register_blueprint(view_api_register, url_prefix='/api/v1')
    app.register_blueprint(view_api_ticket_create, url_prefix='/api/v1')
    app.register_blueprint(view_api_ticket_get, url_prefix='/api/v1')
    app.register_blueprint(view_api_ticket_status, url_prefix='/api/v1')
    return app