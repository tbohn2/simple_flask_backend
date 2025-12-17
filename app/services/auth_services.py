from ..models.user import User
import bcrypt
import jwt
import datetime

SECRET_KEY = "supersecretkey"

# In-memory store for demo
users_db = {
    "test@test.com": User(id=1, name="Test User", email="test@test.com", password="password"),
    "test2@test.com": User(id=2, name="Test User 2", email="test2@test.com", password="password2"),
}

def signup_user(name, email, password):
    user = User(id=len(users_db)+1, name=name, email=email, password=password)
    users_db[email] = user
    return user

def login_user(email, password):
    user = users_db.get(email)
    if user and user.check_password(password):
        # Generate JWT token
        payload = {"user_id": user.id, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return token
    return None
