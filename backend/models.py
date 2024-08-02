# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

class Road(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    end_location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    distance = db.Column(db.Float, nullable=False)
    traffic_condition = db.Column(db.String(50), nullable=False, default="clear")
    start_location = db.relationship("Location", foreign_keys=[start_location_id])
    end_location = db.relationship("Location", foreign_keys=[end_location_id])

class TrafficUpdate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    road_id = db.Column(db.Integer, db.ForeignKey('road.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    traffic_condition = db.Column(db.String(50), nullable=False)
    road = db.relationship("Road", backref=db.backref("traffic_updates", lazy=True))
