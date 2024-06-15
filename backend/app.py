from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./teste.db'
db=SQLAlchemy(app)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    debug = os.environ["FLASK_ENV"] == "development"
    app.run(debug=True, host='0.0.0.0', port=8000)

import controllers.ride_controller
import models.ride
import models.vehicle