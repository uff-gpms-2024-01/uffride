from flask import (
    Blueprint,
    request,
    jsonify,
)
from flask_login import login_required, current_user

from src.services import ride_service
from src.services.offer_ride_service import OfferRideService
from src.services.request_ride_service import RequestRideService

ride_bp = Blueprint("ride", __name__)


@ride_bp.route("/ride/<id>", methods=["GET"])
def get(id):
    return jsonify(ride_service.get_ride(id))


@ride_bp.route("/ride/current", methods=["GET"])
def get_current():
    return jsonify(ride_service.get_current_rides())


@ride_bp.route("/rides", methods=["GET"])
def getAll():
    return jsonify(ride_service.get_all_rides())


@ride_bp.route("/ride", methods=["POST"])
def post():
    return jsonify(ride_service.add_ride(request.json))


@ride_bp.route("/ride/<id>", methods=["PUT"])
def put(id):
    return jsonify(ride_service.update_ride(id))


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

    ride_offered = OfferRideService().offer_ride(
        where_address,
        where_lat,
        where_long,
        to_where_address,
        to_where_lat,
        to_where_long,
        driver,
        vehicle_id,
    )

    return jsonify(ride_offered)


@ride_bp.route("/ride/request", methods=["POST"])
def request_ride():
    user_id = request.json.get("user_id")
    where_address = request.json.get("where_address")
    where_lat = request.json.get("where_lat")
    where_long = request.json.get("where_long")

    to_where_address = request.json.get("to_where_address")
    to_where_lat = request.json.get("to_where_lat")
    to_where_long = request.json.get("to_where_long")

    number_of_passengers = request.json.get("number_of_passengers")
    try:
        number_of_passengers = int(number_of_passengers)
    except ValueError:
        return jsonify({"error": "number_of_passengers must be an integer"}), 400

    requested_ride = RequestRideService().request_ride(
        where_address=where_address,
        where_lat=where_lat,
        where_long=where_long,
        to_where_address=to_where_address,
        to_where_lat=to_where_lat,
        to_where_long=to_where_long,
        number_of_passengers=number_of_passengers,
        user_id=int(user_id),
    )

    return (jsonify(requested_ride)), 201
