from flask import Flask
from backend.config import Config
from backend.models import db
from backend.routes import routes

# Create the Flask application instance
app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database with the app
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(routes)

# Run the app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
