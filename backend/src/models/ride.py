from src import db
from datetime import datetime


class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver = db.Column(db.Integer, nullable=False)
    vehicle_id = db.Column(db.Integer, nullable=False)
    where_address = db.Column(db.String(255), nullable=False)
    where_lat = db.Column(db.Float, nullable=False)
    where_long = db.Column(db.Float, nullable=False)
    to_where_address = db.Column(db.String(255), nullable=False)
    to_where_lat = db.Column(db.Float, nullable=False)
    to_where_long = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "driver": self.driver,
            "vehicle_id": self.vehicle_id,
            "where_address": self.where_address,
            "where_lat": self.where_lat,
            "where_long": self.where_long,
            "to_where_address": self.to_where_address,
            "to_where_lat": self.to_where_lat,
            "to_where_long": self.to_where_long,
            "created_at": self.created_at
        }

    def __repr__(self):
        return "<Ride %r>" % self.id

    
    def __init__(self, data):
        self.driver = data.get("driver")
        self.vehicle_id = data.get("vehicle_id")
        self.where_address = data.get("where_address")
        self.where_lat = data.get("where_lat")
        self.where_long = data.get("where_long")
        self.to_where_address = data.get("to_where_address")
        self.to_where_lat = data.get("to_where_lat")
        self.to_where_long = data.get("to_where_long")
        self.created_at = datetime.now()
        
        return self.to_dict()

        

        
