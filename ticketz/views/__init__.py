from ticketz.views.ui.index import view_ui_index

def build_views(app):
    app.register_blueprint(view_ui_index)
    return app