from datetime import datetime  # Ensure this import is correct
from flask import Blueprint, request, jsonify
from backend import db
from backend.models import Location, Road, TrafficUpdate
from backend.utils import calculate_shortest_path
from sqlalchemy.exc import StatementError

# Define the blueprint
routes = Blueprint('routes', __name__)

@routes.route('/locations', methods=['POST'])
def add_location():
    data = request.json
    location = Location(name=data['name'], latitude=data['latitude'], longitude=data['longitude'])
    db.session.add(location)
    db.session.commit()
    return jsonify(location.id), 201

@routes.route('/roads', methods=['POST'])
def add_road():
    data = request.json
    road = Road(
        start_location_id=data['start_location_id'],
        end_location_id=data['end_location_id'],
        distance=data['distance'],
        traffic_condition=data.get('traffic_condition', 'clear')
    )
    db.session.add(road)
    db.session.commit()
    return jsonify(road.id), 201

@routes.route('/traffic-updates', methods=['POST'])
def update_traffic():
    data = request.json
    
    try:
        # Convert timestamp from string to datetime object
        timestamp = datetime.strptime(data['timestamp'], "%Y-%m-%dT%H:%M:%SZ")
        
        traffic_update = TrafficUpdate(
            road_id=data['road_id'],
            timestamp=timestamp,  # use the converted datetime object here
            traffic_condition=data['traffic_condition']
        )
        
        db.session.add(traffic_update)
        db.session.commit()
        
        return jsonify({"message": "Traffic update created successfully"}), 201
    
    except StatementError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@routes.route('/shortest-path', methods=['GET'])
def get_shortest_path():
    start_location_id = request.args.get('start_location_id')
    end_location_id = request.args.get('end_location_id')

    locations = Location.query.all()
    roads = Road.query.all()
    path_info = calculate_shortest_path(locations, roads, int(start_location_id), int(end_location_id))

    return jsonify(path_info), 200

@routes.route('/roads/<int:id>/traffic-condition', methods=['GET'])
def get_traffic_condition(id):
    road = Road.query.get(id)
    if road:
        return jsonify({"traffic_condition": road.traffic_condition}), 200
    return jsonify({"error": "Road not found"}), 404

@routes.route('/report/traffic', methods=['GET'])
def generate_traffic_report():
    roads = Road.query.all()
    traffic_report = [{"road_id": road.id, "traffic_condition": road.traffic_condition} for road in roads]
    return jsonify(traffic_report), 200
