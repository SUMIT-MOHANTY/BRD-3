from app.models import users_db
from app.utils.auth import hash_password, verify_password, generate_token

class AuthService:
    @staticmethod
    def register(email: str, password: str, first_name: str, last_name: str):
        for user in users_db.values():
            if user['email'] == email:
                return None, 'Email already registered'
        
        user_id = len(users_db) + 1
        user = {
            'id': user_id,
            'email': email,
            'password': hash_password(password),
            'first_name': first_name,
            'last_name': last_name,
            'created_at': str(datetime.now())
        }
        users_db[email] = user
        
        token = generate_token(user_id, email)
        return {'user': user, 'token': token}, None
    
    @staticmethod
    def login(email: str, password: str):
        user = users_db.get(email)
        
        if not user or not verify_password(password, user['password']):
            return None, 'Invalid email or password'
        
        token = generate_token(user['id'], user['email'])
        return {'user': user, 'token': token}, None
    
    @staticmethod
    def get_current_user(email: str):
        user = users_db.get(email)
        if not user:
            return None
        return {k: v for k, v in user.items() if k != 'password'}

from datetime import datetime
