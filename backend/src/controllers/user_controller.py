from flask import (
    Blueprint,
    flash,
    request,
    jsonify,
)
from flask_login import login_required, login_user, logout_user, current_user
from src import bcrypt, db
from src.models import User


user_bp = Blueprint("user", __name__)


@user_bp.route("/user/register", methods=["POST"])
def register():
    if current_user.is_authenticated:
        flash("You are already registered.", "info")
        return jsonify(current_user.to_dict())

    def validate(json):
        return True, ""

    is_valid, errors = validate(request.json)
    if not is_valid:
        return jsonify({"message": "".join(errors)}), 400

    user = User(
        email=request.json.get("email"),
        password=request.json.get("password"),
        name=request.json.get("name"),
    )
    db.session.add(user)
    db.session.commit()

    # Force está como true para fazer login de users com is_active=False
    login_user(user, force=True)
    flash("You registered and are now logged in. Welcome!", "success")

    return jsonify(user.to_dict())


@user_bp.route("/user/login", methods=["POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return jsonify(current_user.to_dict())

    user = User.query.filter_by(email=request.json.get("email")).first()
    if not user and not bcrypt.check_password_hash(
        user.password, request.form["password"]
    ):
        return jsonify({"message": "Invalid email or password."}), 401
    login_user(user, force=True)
    flash("You were logged in.", "success")
    return jsonify(user.to_dict())


@user_bp.route("/user/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return jsonify({"message": "You were logged out."})
