#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Must be empty for the checker
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    # Safely parse JSON
    user_data = request.get_json(silent=True)
    if user_data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check for username key
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check for duplicate user
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Save user
    users[username] = user_data

    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


if __name__ == "__main__":
    app.run()
