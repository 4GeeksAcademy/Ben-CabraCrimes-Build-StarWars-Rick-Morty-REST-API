"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, People, Location, Favourites
from api.utils import generate_sitemap, APIException

api = Blueprint("api", __name__)


@api.route("/hello", methods=["POST", "GET"])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }
    return jsonify(response_body), 200


# GET ALL PEOPLE
@api.route("/people", methods=["GET"])
def get_all_people():
    people = People.query.all()
    people_serialized = [people.serialize() for people in people]
    return jsonify({"people": people_serialized}), 200


# GET ONE PERSON
@api.route("/person/<int:person_id>", methods=["GET"])
def get_one_person(person_id):
    person = People.query.get(person_id)
    if not person:
        return jsonify({"error": "No person with this id found"}), 400
    return jsonify({"person": person.serialize()}), 200


# GET ALL LOCATIONS
@api.route("/location", methods=["GET"])
def get_all_location():
    location = Location.query.all()
    location_serialized = [location.serialize() for location in location]
    return jsonify({"location": location_serialized}), 200


# GET ONE LOCATION
@api.route("/location/<int:location_id>", methods=["GET"])
def get_one_location(location_id):
    location = Location.query.get(location_id)
    if not location:
        return jsonify({"error": "No location with this id found"}), 400
    return jsonify({"person": location.serialize()}), 200


# POST CREATE A PERSON
@api.route("/people", methods=["POST"])
def create_person():
    body = request.json
    new_person = People(
        name=body["name"],
        status=body["status"],
        species=body["species"],
    )
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"people": "create"}), 200


# POST favourites people
@api.route("<int:user_id>/favorites/people/<int:people_id>", methods=["POST"])
def add_people_favourites(people_id):
    # favourite = Favourites(
    #     user_id=request.json["user_id"], people_id=request.json["people_id"]
    # )
    favourite = Favourites(people_id=people_id, user_id=1)
    db.session.add(favourite)
    db.session.commit()
    return jsonify({"favourite": f"Person {people_id} added to favourites {people_id}"})


# CREATE/POST FAVOURITE LOCATION
@api.route("<int:user_id>/favorites/location/<int:location_id>", methods=["POST"])
def add_location_favourites(location_id):
    # favourite = Favourites(
    #     user_id=request.json["user_id"], location_id=request.json["location_id"]
    # )
    favourite = Favourites(location_id=location_id, user_id=1)
    db.session.add(favourite)
    db.session.commit()
    return jsonify(
        {
            "favourite location": f"Location id {location_id} added to favourites {location_id}"
        }  # return all favourites
    )


######EXAMPLE######
# POST ONE FAVOURITE PEOPLE
# @api.route("/favorite/people/<int:people_id> ", methods=["POST"])
# def add_location_favourites(people_id):
#     people = People(people_id=people_id, user_id=1)
#     db.session.add(people)
#     db.session.commit()
#     return jsonify(
#         {
#             "favourite person": f"Person id {people_id} added to favourites {People.all()}"
#         }
#     )


# GET ALL USER FAVOURITE LOCATIONS
@api.route("/favorites/location", methods=["GET"])
def get_all_favourite_locations():
    # location = Favourites.query.filter_by(location_id=1, user_id=1)
    location = Favourites.query.all()
    location_serialized = [location.serialize() for location in location]
    return jsonify({"Favourite location": location_serialized}), 200


# GET ALL THE FAVOURIRES
@api.route("/favourites", methods=["GET"])
def get_user_favourites():
    user_favourites = Favourites.query.all()
    user_favourites_serialized = [user.serialize() for user in user_favourites]
    if not user_favourites:
        return jsonify({"error": "No favourites found"}), 400
    return jsonify({"favourite": user_favourites_serialized}), 200


# GET USER FAVOURITE PEOPLE
@api.route("/favorites/people", methods=["GET"])
def get_location_favourites():
    location_favourites = Favourites.query.all()
    # use filter_by to find correct user
    user_favourites_serialized = [fav.serialize() for fav in location_favourites]
    if not location_favourites:
        return jsonify({"error": "No favourites found"}), 400
    return jsonify({"favourite": user_favourites_serialized}), 200


# GET ONE USER
@api.route("/user/<int:user_id>", methods=["GET"])
def get_one_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "No user with this id found"}), 400
    return jsonify({"person": user.serialize()}), 200


# GET ALL USER
@api.route("/user", methods=["GET"])
def get_all_users():
    user = User.query.all()
    user_serialized = [user.serialize() for user in user]
    return jsonify({"people": user_serialized}), 200


# DELETE A FAVOURITE PEOPLE/PERSON
@api.route("/favourites/people/<int:people_id>", methods=["DELETE"])
def delete_one_people(people_id):
    people = Favourites.query.filter_by(people_id=people_id).first()
    if not people:
        return jsonify({"error": "No people with this id found"}), 400
    db.session.delete(people)
    db.session.commit()
    return jsonify({"person": "people deleted"}), 200


# DELETE A FAVOURITE LOCATION
@api.route("<int:user_id>/favourites/location/<int:location_id>", methods=["DELETE"])
def delete_one_location(location_id, user_id):
    location = Favourites.query.filter_by(
        location_id=location_id, user_id=user_id
    ).first()
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    if not location:
        return jsonify({"error": "No location with this id found"}), 400
    db.session.delete(location)
    db.session.commit()
    return jsonify({"location": "location deleted"}), 200
