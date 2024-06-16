from src import db


class UserRating(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    id_ride = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id_user": self.id_user,
            "id_ride": self.id_ride,
            "rating": self.rating,
        }

    def __repr__(self):
        return f"<UserRating id_user={self.id_user} id_ride={self.id_ride}>"



    def __init__(self, id_user, id_ride, rating):
        super().__init__()
        self.id_user = id_user
        self.id_ride = id_ride
        self.rating = rating
