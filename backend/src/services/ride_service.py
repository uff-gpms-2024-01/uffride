from src import db
from src.models import Ride,User
from datetime import datetime
from sqlalchemy import desc


def get_ride(ride_id):
    try:
        ride = Ride.query.filter_by(id=ride_id).first()
        return ride.to_dict()
    except Exception:
        return "Ride not found"

def get_current_rides():
    try:
        ride = Ride.query.order_by(desc('created_at')).first()
        ride = ride.to_dict()
        new_ride = {}
        new_ride["id"] = ride["id"]
        new_ride["name"] = "Jerson"#User.query.filter_by(id=ride["driver"]).first().name
        new_ride["where"] = ride["where_address"]
        new_ride["toWhere"] = ride["to_where_address"]
        new_ride["ratingQuantity"] = 15
        new_ride["avaiablePlaces"] = 4
        new_ride["rating"] = 3
        new_ride["places"] = 4
        new_ride["date"] = "13-01-2001"
        new_ride["hour"] = "09:30"
        return new_ride
    except Exception:
        return "Ride not found"

def get_all_rides():
    #try:
        rides = Ride.query.all()
        rides_list = [ride.to_dict() for ride in rides]
        response = []
        for ride in rides_list:
            new_ride = {}
            new_ride["id"] = ride["id"]
            new_ride["name"] = "Jerson"#User.query.filter_by(id=ride["driver"]).first().name
            new_ride["where"] = ride["where_address"]
            new_ride["toWhere"] = ride["to_where_address"]
            new_ride["userRating"] = 5#User.query.filter_by(id=ride["driver"]).first().name
            new_ride["ratingQuantity"] = 15
            new_ride["avaiablePlaces"] = 4
            new_ride["rating"] = 3
            new_ride["places"] = 4
            new_ride["date"] = "13-01-2001"
            new_ride["hour"] = "09:30"
            response.append(new_ride)
        return response
    #except Exception:
    #    return "No rides found"


def add_ride(ride_json):
    try:
        ride = Ride(ride_json)
        db.session.add(ride)
        db.session.commit()
        return ride.to_dict()
    except Exception:
        return "Error adding ride"


def update_ride(ride_id):
    try:
        Ride.query.filter_by(id=ride_id).update()
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
