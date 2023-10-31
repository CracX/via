from ticketz.views.ui.index import view_ui_index
from ticketz.views.ui.login import view_ui_login
from ticketz.views.api.v1.login import view_api_login

def build_views(app):
    app.register_blueprint(view_ui_index, url_prefix='/')
    app.register_blueprint(view_ui_login, url_prefix='/login')
    app.register_blueprint(view_api_login, url_prefix='/api/v1')
    return app