from flask import (
    Blueprint,
    flash,
    request,
    jsonify,
)
from src.models import UserRating

from src import bcrypt, db

user_rating = Blueprint("user-rating", __name__)


@user_rating.route("/user-rating/", methods=["POST"])
def post():
    data = request.get_json()
    id_user = data['id_user']
    id_ride = data['id_ride']
    rating = data['rating']
    
    new_rating = UserRating(id_user, id_ride, rating)
        
    try:
        db.session.add(new_rating)
        db.session.commit()
        return jsonify({"message": "User rating created successfully"})

    except Exception as e:
        print(f"Error retrieving user ratings: {e}")

        return f"An error occurred while fetching user ratings: {str(e)}"



@user_rating.route("/user-rating/user/<idUser>/ride/<idRide>/", methods=["GET"])
def get(idUser, idRide):
    try:
        rating = UserRating.query.filter(
            UserRating.id_user == idUser, UserRating.id_ride == idRide
        ).first()

        if rating:
            return jsonify(rating.to_dict())
        else:
            return jsonify({"message": "User rating not found"}), 404

    except Exception as e:
        # Handle potential database errors more gracefully
        print(f"An error occurred: {e}")
        return jsonify({"message": "Internal server error"}), 500


