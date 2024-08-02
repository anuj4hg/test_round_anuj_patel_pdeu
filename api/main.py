from flask import Flask, jsonify, request
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

# Define an endpoint to verify deployment
@app.route('/')
def home():
    return "Flask app is running on Vercel!"

# Function to handle requests
def main(request):
    return app(request)

# If running locally
if __name__ == "__main__":
    app.run(debug=True)
