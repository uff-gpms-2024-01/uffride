from src import db
from src.models import Ride,User,UserRating
from datetime import datetime
import random
from sqlalchemy import desc


def get_ride(ride_id):
    try:
        ride = Ride.query.filter_by(id=ride_id).first()
        return ride.to_dict()
    except Exception:
        return "Ride not found"

def get_current_rides():
    try:
        places = random.randint(1, 4)
        ride = Ride.query.order_by(desc('created_at')).first()
        ride = ride.to_dict()
        new_ride = {}
        new_ride["id"] = ride["id"]
        new_ride["name"] = User.query.filter_by(id=ride["driver"]).first().name
        new_ride["where"] = ride["where_address"]
        new_ride["toWhere"] = ride["to_where_address"]
        new_ride["ratingQuantity"] = random.randint(1, 23)
        new_ride["avaiablePlaces"] = places
        new_ride["rating"] = UserRating.query.filter_by(id_ride=ride["id"]).first().rating
        new_ride["places"] = random.randint(1, places)
        new_ride["date"] = Ride.query.filter_by(id=ride["id"]).first().created_at.strftime("%d-%m-%Y")
        new_ride["hour"] = Ride.query.filter_by(id=ride["id"]).first().created_at.strftime("%H:%M")
        return new_ride
    except Exception:
        return "Ride not found"

def get_all_rides():
    try:
        rides = Ride.query.all()
        rides_list = [ride.to_dict() for ride in rides]
        response = []
        for ride in rides_list:
            places = random.randint(1, 4)
            new_ride = {}
            new_ride["id"] = ride["id"]
            new_ride["name"] = User.query.filter_by(id=ride["driver"]).first().name
            new_ride["where"] = ride["where_address"]
            new_ride["toWhere"] = ride["to_where_address"]
            new_ride["userRating"] = UserRating.query.filter_by(id_ride=ride["id"]).first().rating
            new_ride["ratingQuantity"] = random.randint(1, 23)
            new_ride["avaiablePlaces"] = places
            new_ride["rating"] = random.randint(1, 5)
            new_ride["places"] = random.randint(1, places)
            new_ride["date"] = Ride.query.filter_by(id=ride["id"]).first().created_at.strftime("%d-%m-%Y")
            new_ride["hour"] = Ride.query.filter_by(id=ride["id"]).first().created_at.strftime("%H:%M")
            response.append(new_ride)
        return response
    except Exception:
        return "No rides found"


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
