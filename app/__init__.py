from flask import Flask
import config
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

     # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from app import models
    

    # 블루프린트 등록
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app