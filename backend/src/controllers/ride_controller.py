from src import app
from src.services import ride_service


@app.route("/ride", methods=["GET"])
def get(self):
    if not app.request.args:
        return app.jsonify(ride_service.get_all_rides())
    else:
        return app.jsonify(ride_service.get_ride(app.request.args.get("id")))


@app.route("/ride", methods=["POST"])
def post(self):
    return app.jsonify(ride_service.add_ride(app.request.json))


@app.route("/ride", methods=["PUT"])
def put(self):
    return app.jsonify(
        ride_service.update_ride(app.request.args.get("id"), app.request.json)
    )


@app.route("/ride", methods=["DELETE"])
def delete(self):
    return app.jsonify(ride_service.delete_ride(app.request.args.get("id")))
