# __init__.py
from flask import Flask
from backend.config import Config 
from backend.models import db
from backend.routes import routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(routes)
