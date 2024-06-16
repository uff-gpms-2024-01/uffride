from app import db


def get_ride(self, ride_id):
    try:
        ride = db.session.query(ride).filter_by(id=ride_id).first()
        return ride.to_dict()
    except Exception:
        return "Ride not found"


def get_all_rides(self):
    try:
        rides = db.session.query(rides).all()
        return [ride.to_dict() for ride in rides]
    except Exception:
        return "No rides found"


def add_ride(self, ride):
    try:
        db.session.add(ride)
        db.session.commit()
        return ride.to_dict()
    except Exception:
        return "Error adding ride"


def update_ride(self, ride_id, ride):
    try:
        db.session.query(ride).filter_by(id=ride_id).update(ride)
        db.session.commit()
        return ride.to_dict()
    except Exception:
        return "Error updating ride"


def delete_ride(self, ride_id):
    try:
        ride = db.session.query(ride).filter_by(id=ride_id).first()
        db.session.delete(ride)
        db.session.commit()
        return ride.to_dict()
    except Exception:
        return "Error deleting ride"
