from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def index():
    return "ok"

if __name__ == "__main__":
    debug = os.environ["FLASK_ENV"] == "development"
    app.run(debug=debug, host='0.0.0.0', port=8000)