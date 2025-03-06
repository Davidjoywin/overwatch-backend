from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

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
        beacons = Beacon.getBeaconFromProfile(user)
        beacon_serializer = BeaconSerializer(Beacon.objects.all(), many=True)
        return Response(
            data=beacon_serializer.data,
            status=status.HTTP_200_OK
        )
    
    def put(self, request):
        """
            PUT method :
            user sendin panic alarm - True => panic && False => no panic
        """
        self.check_permissions(request)
        user = request.user
        profile = Profile.objects.get(user=user)
        beacon = Beacon.objects.get(user_profile=profile)
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
    
class GlobalPanicDispatchView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        panic_profiles = Profile.objects.filter(is_panic=True)
        profile_serializer = ProfileSerializer(panic_profiles)
        return Response(
            data=profile_serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request):
        user=request.user
        self.check_object_permissions(request, user)
        try:
            profile=Profile.objects.get(user=user)
            profile.is_valid = True
            profile.save()
            profile_serializer = ProfileSerializer(profile)
            return Response(
                data=profile_serializer.data,
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                data={"error": "Global panic dispatch failed"},
                status=status.HTTP_400_BAD_REQUEST
            )