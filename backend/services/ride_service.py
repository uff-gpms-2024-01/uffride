from models import ride as ride_model
def get_ride(self, ride_id):
    try:
        ride = ride_model.query.filter_by(id=ride_id).first()
        return ride.to_dict()
    except:
        return 'Ride not found'

def get_all_rides():
    try:
        rides = ride_model.query.all()
        return [ride.to_dict() for ride in rides]
    except:
        return 'No rides found'

def add_ride(json_ride):
    ride = ride_model.ride(json_ride)
    try:
        ride_model.add(ride)
        ride_model.commit()
        return ride.to_dict()
    except:
        return 'Error adding ride'

def update_ride(self, ride_id, up_ride):
    try:
        ride = ride_model.query(ride).filter_by(id=ride_id).first()
        ride.driver = up_ride['driver']
        ride.vehicle_id = up_ride['vehicle_id']
        ride.start = up_ride['start']
        ride.end = up_ride['end']
        ride.status = up_ride['status']
        ride_model.commit()
        return ride.to_dict()
    except:
        return 'Error updating ride'

def delete_ride(self, ride_id):
    try:
        ride = ride_model.query(ride).filter_by(id=ride_id).first()
        ride_model.delete(ride)
        ride_model.commit()
        return 'Ride deleted'
    except: 
        return 'Error deleting ride'