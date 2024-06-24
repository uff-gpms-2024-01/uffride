from sqlalchemy import true
from src.models import Ride, RidePassenger
from src import db
from sqlalchemy.exc import SQLAlchemyError


class RequestRideService:
    def request_ride(
        self,
        where_address,
        where_lat,
        where_long,
        to_where_address,
        to_where_lat,
        to_where_long,
        number_of_passengers,
        user_id,
    ):

        with db.session.begin(nested=True) as request_ride_transaction:
            try:
                ride = Ride(
                    {
                        "where_address": where_address,
                        "where_lat": where_lat,
                        "where_long": where_long,
                        "to_where_address": to_where_address,
                        "to_where_lat": to_where_lat,
                        "to_where_long": to_where_long,
                    }
                )

                request_ride_transaction.session.add(ride)
                request_ride_transaction.session.flush()

                for _ in range(number_of_passengers):
                    passenger = RidePassenger(ride_id=ride.id, user_id=user_id)
                    request_ride_transaction.session.add(passenger)

            except SQLAlchemyError as e:
                request_ride_transaction.session.rollback()
                raise e

        return passenger.to_dict()
