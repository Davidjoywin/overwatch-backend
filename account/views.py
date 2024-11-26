from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from utils.token import create_token
from .serializers import AuthSerializer


class Auth(APIView):

    serializer_class = AuthSerializer

    def post(self, request):
        print(request.data)
        username = request.data['username']
        password = request.data['password']

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                token = create_token(user)

                return Response(
                    data=token,
                    status=status.HTTP_200_OK
                )
            return Response(
                data={'error': "password incorrect"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except User.DoesNotExist:
            return Response(
                data={"error": "User Not Found"},
                status=status.HTTP_404_NOT_FOUND
            )
