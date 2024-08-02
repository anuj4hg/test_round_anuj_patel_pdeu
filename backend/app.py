from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from backend.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Define your models
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

class Road(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    end_location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    traffic_condition = db.Column(db.String(20), nullable=False)

class TrafficUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    road_id = db.Column(db.Integer, db.ForeignKey('road.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    traffic_condition = db.Column(db.String(20), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define your routes
@app.route('/locations', methods=['POST'])
def add_location():
    data = request.get_json()
    location = Location(name=data['name'], latitude=data['latitude'], longitude=data['longitude'])
    db.session.add(location)
    db.session.commit()
    return jsonify({'message': 'Location created', 'id': location.id}), 201

@app.route('/roads', methods=['POST'])
def add_road():
    data = request.get_json()
    road = Road(
        start_location_id=data['start_location_id'],
        end_location_id=data['end_location_id'],
        distance=data['distance'],
        traffic_condition=data['traffic_condition']
    )
    db.session.add(road)
    db.session.commit()
    return jsonify({'message': 'Road created', 'id': road.id}), 201

@app.route('/traffic-updates', methods=['POST'])
def update_traffic_condition():
    data = request.get_json()
    traffic_update = TrafficUpdate(
        road_id=data['road_id'],
        timestamp=data['timestamp'],
        traffic_condition=data['traffic_condition']
    )
    db.session.add(traffic_update)
    db.session.commit()
    return jsonify({'message': 'Traffic condition updated', 'id': traffic_update.id}), 201

@app.route('/shortest-path', methods=['GET'])
def get_shortest_path():
    start_location_id = request.args.get('start_location_id')
    end_location_id = request.args.get('end_location_id')
    # Placeholder for pathfinding logic
    path = ["a_location_id", "b_location_id", "c_location_id"]
    total_distance = 10
    estimated_time = 15
    return jsonify({
        'path': path,
        'total_distance': total_distance,
        'estimated_time': estimated_time
    }), 200

@app.route('/roads/<int:id>/traffic-condition', methods=['GET'])
def get_traffic_condition(id):
    road = Road.query.get(id)
    if road:
        return jsonify({
            'road_id': road.id,
            'traffic_condition': road.traffic_condition
        }), 200
    return jsonify({'message': 'Road not found'}), 404

@app.route('/report/traffic', methods=['GET'])
def generate_traffic_report():
    # Placeholder for report generation logic
    # Example: generate a CSV file of all roads and their traffic conditions
    return jsonify({'message': 'Report generation not implemented'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

