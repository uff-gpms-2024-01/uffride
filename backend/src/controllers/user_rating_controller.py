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

    # Create a new UserRating object
    new_rating = UserRating(id_user=id_user, id_ride=id_ride, rating=rating)

    # Add the new object to the session
        
    try:
        db.session.add(new_rating)
        # Commit the changes to the database
        db.session.commit()
        # Return a successful response
        return jsonify({"message": "User rating created successfully"})

    except Exception as e:
        print(f"Error retrieving user ratings: {e}")

        return f"An error occurred while fetching user ratings: {str(e)}"