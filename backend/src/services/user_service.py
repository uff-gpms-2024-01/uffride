from requests import request
from src import bcrypt,db
from src.models import User
from flask import jsonify


def get_user(user_id):
    try:
        user = User.query.filter_by(id=user_id).first()
        return user.to_dict()
    except Exception:
        return "User not found"


def get_all_users():
    try:
        users = User.query.all()
        return [user.to_dict() for user in users]
    except Exception:
        return "No users found"


def update_user(user_id):
    try:
        data = request.json
        update_data = {}

        if "email" in data:
            update_data["email"] = data["email"]
        if "name" in data:
            update_data["name"] = data["name"]

        User.query.filter_by(id=user_id).update(update_data)
        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error updating user", "error": str(e)}), 500