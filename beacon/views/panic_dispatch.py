from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Beacon
from account.models import Profile
from ..serializers import BeaconSerializer
from account.serializers import ProfileSerializer

class PanicDispatchView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """
            GET method:
            Each authenticated user receiving panic alarm 
        """
        user = request.user
        profile = Profile.objects.get(user=user)
        self.check_permissions(request)
        profiles_in_terror = [beacon.user for beacon in profile.getUserInTerror()]
        profile_serializer = ProfileSerializer(profiles_in_terror, many=True)
        return Response(
            data=profile_serializer.data,
            status=status.HTTP_200_OK
        )
    
    def put(self, request):
        """
            PUT method :
            user sendin panic alarm - True => panic && False => no panic
        """
        self.check_permissions(request)
        username = request.user.username
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)
        beacon = Beacon.objects.get(user=profile)
        beacon_serializer = BeaconSerializer(beacon, data=request.data)
        if beacon_serializer.is_valid():
            beacon_serializer.save()
            return Response(
                data=beacon_serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data=beacon_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )