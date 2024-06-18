from decouple import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins='*')
app.config.from_object(config("APP_SETTINGS"))


login_manager = LoginManager()
login_manager.init_app(app)

bcrypt = Bcrypt(app)
db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)

<<<<<<< HEAD
from src.controllers.user_controller import user_bp
from src.controllers.ride_controller import ride_bp  # noqa: E402
=======
from src.controllers.user_controller import user_bp  # noqa: E402
from src.controllers.user_rating_controller import user_rating 
>>>>>>> refs/heads/avaliacao-de-corrida

app.register_blueprint(user_bp, url_prefix="/api")
<<<<<<< HEAD
app.register_blueprint(ride_bp, url_prefix="/api")
=======
app.register_blueprint(user_rating, url_prefix="/api")
>>>>>>> refs/heads/avaliacao-de-corrida

from src.models.user import User  # noqa: E402

login_manager.login_view = "accounts.login"
login_manager.login_message_category = "danger"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


#
