from ticketz.views.ui.index import view_ui_index
from ticketz.views.ui.login import view_ui_login
from ticketz.views.api.v1.login import view_api_login
from ticketz.views.api.v1.register import view_api_register
from ticketz.views.api.v1.create_ticket import view_api_ticket_create

def build_views(app):
    app.register_blueprint(view_ui_index, url_prefix='/')
    app.register_blueprint(view_ui_login, url_prefix='/login')
    app.register_blueprint(view_api_login, url_prefix='/api/v1')
    app.register_blueprint(view_api_register, url_prefix='/api/v1')
    app.register_blueprint(view_api_ticket_create, url_prefix='/api/v1')
    return app