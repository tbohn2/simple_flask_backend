from app.models.user import User

class UserService:
    """Service layer for user business logic"""
    
    def __init__(self):
        # In a real app, this would initialize database connection
        self.users = []
        self.next_id = 1
    
    def get_all_users(self):
        """Get all users"""
        return [user.to_dict() for user in self.users]
    
    def get_user_by_id(self, user_id):
        """Get user by ID"""
        for user in self.users:
            if user.id == user_id:
                return user.to_dict()
        return None
    
    def create_user(self, data):
        """Create a new user"""
        user = User(
            id=self.next_id,
            name=data.get('name'),
            email=data.get('email')
        )
        self.users.append(user)
        self.next_id += 1
        return user.to_dict()

