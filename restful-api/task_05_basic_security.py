#!/usr/bin/python3
"""Module that implements API security with Basic Auth and JWT."""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic auth."""
    if username in users and check_password_hash(
            users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Return access granted message for basic auth."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Login and return a JWT token."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username not in users or not check_password_hash(
            users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(identity={
        "username": username,
        "role": users[username]["role"]
    })
    return jsonify({"access_token": token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Return access granted message for JWT auth."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Return access granted message for admin only."""
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_data):
    """Handle expired token."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_data):
    """Handle revoked token."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_data):
    """Handle needs fresh token."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
