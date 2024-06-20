from src import db
from datetime import datetime
from sqlalchemy.orm import mapped_column, relationship, Mapped
from typing import List
from sqlalchemy import ForeignKey


class Ride(db.Model):
    __tablename__ = "ride"

    id = db.Column(db.Integer, primary_key=True)
    driver = db.Column(db.Integer)
    vehicle_id = db.Column(db.Integer)
    where_address = db.Column(db.String(255), nullable=False)
    where_lat = db.Column(db.Float, nullable=False)
    where_long = db.Column(db.Float, nullable=False)
    to_where_address = db.Column(db.String(255), nullable=False)
    to_where_lat = db.Column(db.Float, nullable=False)
    to_where_long = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    passengers = relationship("RidePassenger", back_populates="ride")

    def to_dict(self):
        return {
            "id": self.id,
            "driver": self.driver,
            "vehicle_id": self.vehicle_id,
            "where_address": self.where_address,
            "where_lat": self.where_lat,
            "where_long": self.where_long,
            "to_where_address": self.to_where_address,
            "to_where_lat": self.to_where_lat,
            "to_where_long": self.to_where_long,
            "created_at": self.created_at,
            "passengers": [passenger.user_id for passenger in self.passengers],
        }

    def __repr__(self):
        return "<Ride %r>" % self.id

    def __init__(self, data):
        self.driver = data.get("driver")
        self.vehicle_id = data.get("vehicle_id")
        self.where_address = data.get("where_address")
        self.where_lat = data.get("where_lat")
        self.where_long = data.get("where_long")
        self.to_where_address = data.get("to_where_address")
        self.to_where_lat = data.get("to_where_lat")
        self.to_where_long = data.get("to_where_long")
        self.created_at = datetime.now()


class RidePassenger(db.Model):
    __tablename__ = "ride_passenger"

    ride_id: Mapped[int] = mapped_column(ForeignKey("ride.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), primary_key=True)

    ride = relationship("Ride", back_populates="passengers")

    def __init__(self, ride_id: int, user_id: int):
        self.ride_id = ride_id
        self.user_id = user_id

    def to_dict(self) -> dict:
        return self.ride.to_dict()
