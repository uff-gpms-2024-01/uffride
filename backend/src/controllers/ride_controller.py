from flask import (
    Blueprint,
    flash,
    request,
    jsonify,
)

from src.services import ride_service
from src.services.offer_ride_service import OfferRideService

ride_bp = Blueprint("ride", __name__)



@ride_bp.route("/ride/<id>", methods=["GET"])
def get(id):
    return jsonify(ride_service.get_ride(id))

@ride_bp.route("/ride", methods=["GET"])
def getAll():    
    return jsonify(ride_service.get_all_rides())


@ride_bp.route("/ride", methods=["POST"])
def post():
    return jsonify(ride_service.add_ride(request.json))


@ride_bp.route("/ride/<id>", methods=["PUT"])
def put(id):
    return jsonify(
        ride_service.update_ride(id)
    )


@ride_bp.route("/ride/<id>", methods=["DELETE"])
def delete(id):
    return jsonify(ride_service.delete_ride(id))

@ride_bp.route("/ride/offer", methods=["POST"])
def offer_ride():
    where_address = request.json.get("where_address")
    where_lat = request.json.get("where_lat")
    where_long = request.json.get("where_long")

    to_where_address = request.json.get("to_where_address")
    to_where_lat = request.json.get("to_where_lat")
    to_where_long = request.json.get("to_where_long")

    driver = request.json.get("driver")
    vehicle_id = request.json.get("vehicle_id")


    rideOffered = OfferRideService().offer_ride(where_address, where_lat, where_long, to_where_address, to_where_lat, to_where_long, driver, vehicle_id)

    return jsonify(rideOffered)
   