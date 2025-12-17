from flask import Blueprint, request, jsonify
from ..services.auth_service import signup_user, login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    user = signup_user(data["name"], data["email"], data["password"])
    return jsonify(user.to_dict()), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    token = login_user(data["email"], data["password"])
    if token:
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401
