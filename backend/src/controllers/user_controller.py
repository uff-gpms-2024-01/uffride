import re
from flask import (
    Blueprint,
    flash,
    redirect,
    request,
    jsonify,
)
from flask_login import login_required, login_user, logout_user, current_user
from src import bcrypt, db
from src.models import User
from src.services import user_service


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

    return jsonify(user.to_dict()), 201


@user_bp.route("/user/login", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return redirect("/#/login")

    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return jsonify(current_user.to_dict())

    user = User.query.filter_by(email=request.json.get("email")).first()

    if not user or not bcrypt.check_password_hash(
        user.password, request.json.get("password")
    ):
        return (
            jsonify({"message": "Não há usuário para as credenciais fornecidas."}),
            401,
        )
    login_user(user, force=True)
    flash("You were logged in.", "success")
    return jsonify(user.to_dict())


@user_bp.route("/user/logout")
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return jsonify({"message": "You were logged out."})

@user_bp.route("/user/<user_id>", methods=["GET"])
@login_required
def get(user_id):
    user = user_service.get_user(user_id)
    return jsonify(user)


'''@user_bp.route("/user/list", methods=["GET"])
@login_required
def list_users():
    users = User.get_all_users()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list)'''


'''
@user_bp.route("/users/search", methods=["GET"])
@login_required
def search_users():
    query_param = request.args.get("q")
    if not query_param:
        return jsonify({"message": "Query parameter 'q' is required."}), 400
    
    users = User.query.filter(
        (User.email.ilike(f"%{query_param}%")) |
        (User.name.ilike(f"%{query_param}%"))
    ).all()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list)
    '''


@user_bp.route("/user/<int:user_id>", methods=["PUT"])
@login_required
def update_user(user_id):
    data = request.get_json()
    print(data)
    result = user_service.update_user(user_id, data)
    # if user != current_user:
    #     return jsonify({"message": "You can only update your own profile."}), 403
    return result
