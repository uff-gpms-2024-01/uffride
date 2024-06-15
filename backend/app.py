from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db=SQLAlchemy(app)

@app.route("/")
def index():
    return "ok"

if __name__ == "__main__":
    debug = os.environ["FLASK_ENV"] == "development"
    app.run(debug=True, host='0.0.0.0', port=8000)
