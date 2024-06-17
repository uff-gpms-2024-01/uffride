from app import app
from services import ride_service
from flask import request

@app.route("/ride/<int:id>", methods=["GET"])
def get(id):
    assert id == request.view_args['id']
    if id == None:
        return ride_service.get_all_rides()
    else:    
        return ride_service.get_ride(request.args.get('id'))

@app.route("/ride", methods=["POST"])
def post():
    return ride_service.add_ride(request.get_json())

@app.route("/ride/<int:id>", methods=["PUT"])
def put():
    if app.request.args.get('id') == None:
        return 'Please provide an id'
    return ride_service.update_ride(app.request.args.get('id'), app.request.json)

@app.route("/ride/<int:id>", methods=["DELETE"])
def delete():
    if app.request.args.get('id') == None:
        return 'Please provide an id'
    return ride_service.delete_ride(app.request.args.get('id'))