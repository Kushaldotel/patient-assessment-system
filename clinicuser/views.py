from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.views import APIView

User = get_user_model()


@api_view(["POST"])
def user_registration(request):
    data = request.data
    # import pdb; pdb.set_trace()
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  # Save the user instance

        response_data = {
            "message": "User Successfully Registerecd",
            "user_data": serializer.data,
        }
        return Response(data=response_data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = authenticate(request, email=email, password=password)
        if user is not None:
            # User authenticated successfully
            access_token = AccessToken.for_user(user)
            refresh_token = RefreshToken.for_user(user)

            response_data = {
                "message": "User authenticated successfully",
                "access_token": str(access_token),
                "refresh_token": str(refresh_token),
                "email": user.email,
                "address": user.address,
                "phone": str(user.phone),
            }

            return Response(data=response_data)
        else:
            response_data = {
                "message": "Invalid credentials",
            }
            return Response(data=response_data, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT, data={"message": "Logout successful"})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": "Invalid token"})