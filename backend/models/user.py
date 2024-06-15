from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }
    def __repr__(self):
        return '<User %r>' % self.id
    
    def __init__(self,dicio):
        super().__init__()
        self.id = dicio["id"]
        self.name = dicio["name"]
        self.email = dicio["email"]