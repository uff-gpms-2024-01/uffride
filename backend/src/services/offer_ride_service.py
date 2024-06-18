from src.models import Ride
from src import db

class OfferRideService:

    
    def __init__(self):
        pass

    def offer_ride(self, where_address, where_lat, where_long, to_where_address, to_where_lat, to_where_long, driver, vehicle_id):
        ride = Ride({
            "where_address": where_address,
            "where_lat": where_lat,
            "where_long": where_long,
            "to_where_address": to_where_address,
            "to_where_lat": to_where_lat,
            "to_where_long": to_where_long,
            "driver": driver,
            "vehicle_id": vehicle_id
        })

        db.session.add(ride)

        db.session.commit()

        return ride.to_dict()