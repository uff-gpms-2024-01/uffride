from src import db


class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    driver_id = db.Column(db.Integer, nullable=False)
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
        return "<Vehicle %r>" % self.id

    def __init__(self, dicio):
        super().__init__()
        self.id = dicio["id"]
        self.driver_id = dicio["driver_id"]
        self.model = dicio["model"]
        self.num_passangers = dicio["num_passangers"]
        self.color = dicio["color"]
        self.license_plate = dicio["license_plate"]
