from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import BeaconSerializer

from account.models import Profile
from ..serializers import SecuritySerializer


class ChangePinView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, reqeust):...

    def put(self, request):
        user = request.user
        profile = Profile.object.get(user=user)
        self.check_object_permissions(request, profile)
        serializer = SecuritySerializer(profile, request.data)
        if serializer.is_valid():
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data=serializer.error,
            status=status.HTTP_400_BAD_REQUEST
        )