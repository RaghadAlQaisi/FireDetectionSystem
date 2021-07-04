from flask import Blueprint, request, jsonify
from flask import current_app as app
import json

main_bp = Blueprint('main_bp', __name__)

# Ping Route
@main_bp.route('/')
def api_ping():
    response = {
        "success": True,
        "code": 200,
        "description": "Availabe routes: ['/alert/*', '/cameras/*]."
        }
    return jsonify(response)
