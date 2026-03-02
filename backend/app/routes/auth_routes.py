from flask import request, jsonify
from marshmallow import ValidationError as MarshmallowValidationError
from app.routes import auth_bp
from app.schemas import RegisterSchema, LoginSchema
from app.services.auth_service import AuthService
from app.utils.auth import token_required

register_schema = RegisterSchema()
login_schema = LoginSchema()

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = register_schema.load(request.get_json())
    except MarshmallowValidationError as e:
        return jsonify({'error': 'Validation error', 'details': e.messages, 'success': False}), 400
    
    user, error = AuthService.register(
        email=data['email'],
        password=data['password'],
        first_name=data['first_name'],
        last_name=data['last_name']
    )
    
    if error:
        return jsonify({'error': error, 'success': False}), 409
    
    user_data = {k: v for k, v in user['user'].items() if k != 'password'}
    return jsonify({
        'data': {'user': user_data, 'token': user['token']},
        'message': 'Registration successful',
        'success': True
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = login_schema.load(request.get_json())
    except MarshmallowValidationError as e:
        return jsonify({'error': 'Validation error', 'details': e.messages, 'success': False}), 400
    
    user, error = AuthService.login(email=data['email'], password=data['password'])
    
    if error:
        return jsonify({'error': error, 'success': False}), 401
    
    user_data = {k: v for k, v in user['user'].items() if k != 'password'}
    return jsonify({
        'data': {'user': user_data, 'token': user['token']},
        'message': 'Login successful',
        'success': True
    }), 200

@auth_bp.route('/logout', methods=['POST'])
@token_required
def logout():
    return jsonify({
        'message': 'Logout successful',
        'success': True
    }), 200

@auth_bp.route('/me', methods=['GET'])
@token_required
def get_current_user():
    email = request.current_user.get('email')
    user = AuthService.get_current_user(email)
    
    if not user:
        return jsonify({'error': 'User not found', 'success': False}), 404
    
    return jsonify({
        'data': user,
        'success': True
    }), 200
