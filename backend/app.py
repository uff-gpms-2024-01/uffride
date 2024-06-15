from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///uffride.db"
db = SQLAlchemy()


db.init_app(app)

with app.app_context():
    db.create_all()
if __name__ == "__main__":
    debug = os.environ["FLASK_ENV"] == "development"
    app.run(debug=True, host="0.0.0.0", port=8000)
