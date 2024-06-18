from src import bcrypt, db
from datetime import datetime
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at,
        }

    def __repr__(self):
        return "<User %r>" % self.id

    def __init__(
        self,
        name: str,
        email: str,
        password: str,
        created_at: datetime = datetime.now(),
    ):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_at = created_at
