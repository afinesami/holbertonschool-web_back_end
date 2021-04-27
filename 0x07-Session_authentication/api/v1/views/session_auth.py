#!/usr/bin/env python3
""" sesion auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ GET /api/v1/users
    Return:
      - list of all User objects JSON represented
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})

    if not users:
        return jsonify(error="no user found for this email"), 404

    for user in users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        else:
            from api.v1.app import auth
            sesion_id = auth.create_session(user.id)
            sesion_name = os.getenv("SESSION_NAME")
            user_dict = jsonify(user.to_json())
            user_dict.set_cookie(sesion_name, sesion_id)
            return user_dict


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def logout():
    '''self descriptive'''
    destroy_session = auth.destroy_session(request)

    if destroy_session:
        return jsonify({}), 200
    abort(404)
