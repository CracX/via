from flask import Flask
from ticketz.models import db
from ticketz.views import build_views

def build_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app = build_views(app)
    return app

if __name__=="__main__":
    app = build_app()
    with app.app_context():
        db.init_app(app)
        db.create_all()
    app.run()
