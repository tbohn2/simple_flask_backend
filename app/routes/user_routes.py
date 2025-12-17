from flask import Blueprint, jsonify, request
from app.services.user_service import UserService
from app.utils.auth import check_token

bp = Blueprint('users', __name__, url_prefix='/api/users')
user_service = UserService()

@bp.before_request
def check_auth():
    if request.endpoint != 'auth.signup' and request.endpoint != 'auth.login':
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "Unauthorized"}), 401
        payload = check_token(token)
        if not payload:
            return jsonify({"error": "Unauthorized"}), 401

@bp.route('/', methods=['GET'])
def get_users():
    """Get all users"""
    try:
        users = user_service.get_all_users()
        return jsonify({
            'status': 'success',
            'data': users
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    try:
        user = user_service.get_user_by_id(user_id)
        if user:
            return jsonify({
                'status': 'success',
                'data': user
            }), 200
        else:
            return jsonify({
                'status': 'error',
                'message': 'User not found'
            }), 404
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@bp.route('/', methods=['POST'])
def create_user():
    """Create a new user"""
    try:
        data = request.get_json()
        user = user_service.create_user(data)
        return jsonify({
            'status': 'success',
            'data': user,
            'message': 'User created successfully'
        }), 201
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

