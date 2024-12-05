from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Profile
from utils.token import create_token
from .serializers import AuthSerializer, UserProfileSerializer, RegisterUserSerializer


class AuthView(APIView):

    serializer_class = AuthSerializer

    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                token = create_token(user)

                return Response(
                    data=token,
                    status=status.HTTP_200_OK
                )
            return Response(
                data={'error': "Authentication failed due to incorrect password"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except User.DoesNotExist:
            return Response(
                data={"error": "User Not Found"},
                status=status.HTTP_404_NOT_FOUND
            )


class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class UserView(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            profile = Profile.objects.get(user=user)
            serializer = UserProfileSerializer(profile)
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        except User.DoesNotExit:
            Response(
                data={"error": "User does not exit"},
                status= status.HTTP_404_NOT_FOUND
            )
