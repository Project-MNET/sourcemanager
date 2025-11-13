from flask_sqlalchemy import SQLAlchemy
import os
db = SQLAlchemy()
def init(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    app.config.setdefault("SQLALCHEMY_ENGINE_OPTIONS", {"pool_pre_ping": True})
    db.init_app(app)

