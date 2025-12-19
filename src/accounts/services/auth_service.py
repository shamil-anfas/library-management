from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User

class AuthService:

    @staticmethod
    def signup_user(data):
        """
        Create a new user with hashed password
        """
        user = User(
            username=data['username'],
            email=data['email'],
            phone=data.get('phone')
        )
        user.set_password(data['password'])
        user.save()
        return user
    
    @staticmethod
    def login_user(username, password):
        """
        Authenticate user and return JWT tokens
        """
        user = authenticate(username=username, password=password)

        if not user:
            return None

        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": user
        }
    

    @staticmethod
    def logout_user(refresh_token):
        """
        Blacklist the provided refresh token
        """
        token = RefreshToken(refresh_token)
        token.blacklist()
