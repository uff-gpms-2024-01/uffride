from src import db
from datetime import datetime


class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver = db.Column(db.Integer, nullable=False)
    vehicle_id = db.Column(db.Integer, nullable=False)
    start = db.Column(db.DateTime(50), nullable=False)
    end = db.Column(db.DateTime(50),nullable=True)
    status = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "driver": self.driver,
            "vehicle_id": self.vehicle_id,
            "start": self.start,
            "end": self.end,
            "status": self.status,
        }

    def __repr__(self):
        return "<Ride %r>" % self.id

    def __init__(self, id: int, driver: int, vehicle_id: int, status: str, start: datetime, end: datetime):
        super().__init__()
        self.id = id
        self.driver = driver
        self.vehicle_id = vehicle_id
        if start != None:
            self.start = start
        self.end = end
        self.status = status
