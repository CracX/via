from ticketz.views.ui.index import view_ui_index
from ticketz.views.ui.login import view_ui_login

def build_views(app):
    app.register_blueprint(view_ui_index, url_prefix='/')
    app.register_blueprint(view_ui_login, url_prefix='/login')
    return app