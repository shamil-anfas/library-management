from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer,LoginSerializer,LogoutSerializer
from .services.auth_service import AuthService
from rest_framework.permissions import IsAuthenticated


class SignupView(APIView):

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = AuthService.signup_user(serializer.validated_data)

        return Response(
            {
                "message": "User registered successfully",
                "username": user.username,
                "email": user.email
            },
            status=status.HTTP_201_CREATED
        )
    

class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = AuthService.login_user(
            serializer.validated_data['username'],
            serializer.validated_data['password']
        )

        if not result:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response({
            "access": result["access"],
            "refresh": result["refresh"]
        })
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        AuthService.logout_user(serializer.validated_data['refresh'])

        return Response({"message": "Logged out successfully"})