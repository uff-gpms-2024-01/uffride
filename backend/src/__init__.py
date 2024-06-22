from decouple import config
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*")
app.config.from_object(config("APP_SETTINGS"))


login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)
db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)

from src.controllers.ride_controller import ride_bp  # noqa: E402
from src.controllers.user_controller import user_bp  # noqa: E402
from src.controllers.user_rating_controller import user_rating

app.register_blueprint(user_bp, url_prefix="/api")
app.register_blueprint(ride_bp, url_prefix="/api")
app.register_blueprint(user_rating, url_prefix="/api")

from src.models.user import User  # noqa: E402

login_manager.login_view = "user.login"
login_manager.login_message_category = "danger"

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)


# enable CORS
@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    return response


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
