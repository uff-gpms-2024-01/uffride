from app import db

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver = db.Column(db.String(50), nullable=False)
    vehicle_id = db.Column(db.Integer, nullable=False)
    start = db.Column(db.String(50), nullable=False)
    end = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    def to_dict(self):
        return {
            "id": self.id,
            "driver": self.driver,
            "vehicle_id": self.vehicle_id,
            "start": self.start,
            "end": self.end,
            "status": self.status
        }
    def __repr__(self):
        return '<Ride %r>' % self.id