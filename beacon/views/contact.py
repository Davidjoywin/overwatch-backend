from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from utils.helpers import beacon_search
from account.serializers import ProfileSerializer


class SearchBeaconListView(APIView):
    def get(self, request):
        """
        search: beacon/search/?profile
        """
        profile_search = request.GET.get('profile', '')
        user = User.objects.get(username=request.user.username).profile
        profiles = beacon_search(user, profile_search)
        profile_serializer = ProfileSerializer(profiles, many=True)
        return Response(
            data=profile_serializer.data,
            status=status.HTTP_200_OK
        )
        
        