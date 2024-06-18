from flask import (
    Blueprint,
    flash,
    request,
    jsonify,
)

from src.services import ride_service
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
