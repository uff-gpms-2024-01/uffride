from src import db
from src.models import Ride
from datetime import datetime


def get_ride(ride_id):
    try:
        ride = Ride.query.filter_by(id=ride_id).first()
        return ride.to_dict()
    except Exception:
        return "Ride not found"


def get_all_rides():
    try:
        rides = Ride.query.all()
        return [ride.to_dict() for ride in rides]
    except Exception:
        return "No rides found"


def add_ride(ride_json):
    try:
        ride = Ride(ride_json.get("id"), ride_json.get("driver"), ride_json.get("vehicle_id"), ride_json.get("status"),datetime.now(),None)
        db.session.add(ride)
        db.session.commit()
        return ride.to_dict()
    except Exception:
        return "Error adding ride"


def update_ride(ride_id):
    try:
        Ride.query.filter_by(id=ride_id).update({"end": datetime.now(), "status": "completed"})
        db.session.commit()
        return "Ride updated successfully"
    except Exception:
        return "Error updating ride"


def delete_ride(ride_id):
    try:
        ride = Ride.query.filter_by(id=ride_id).first()
        db.session.delete(ride)
        db.session.commit()
        return ride.to_dict()
    except Exception:
        return "Error deleting ride"
