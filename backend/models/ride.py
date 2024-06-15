from app import db
import models.vehicle as vehicle

class ride(db.Model):
    __tablename__ = 'ride'

    id = db.Column(db.Integer, primary_key=True)
    driver = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
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
    
    def __init__(self,dicio):
        super().__init__()
        self.id = dicio["id"]
        self.driver = dicio["driver"]
        self.vehicle_id = dicio["vehicle_id"]
        self.start = dicio["start"]
        self.end = dicio["end"]
        self.status = dicio["status"]