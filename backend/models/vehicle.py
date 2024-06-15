from app import db

class vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'), nullable=False)
    num_passangers = db.Column(db.Integer, nullable=False)
    model = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    license_plate = db.Column(db.String(50), nullable=False)
    def to_dict(self):
        return {
            "id": self.id,
            "driver_id": self.driver_id,
            "model": self.model,
            "num_passangers": self.num_passangers,
            "color": self.color,
            "license_plate": self.license_plate,
        }
    def __repr__(self):
        return '<Vehicle %r>' % self.id
