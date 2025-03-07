from django.test import TestCase

from django.contrib.auth.models import User
from account.models import Profile
from beacon.models import Beacon

david = User.objects.get(username='david').profile
beacon = Beacon.objects.get(user=david)

def get_beacon_profiles(user):
    profiles = None
    try:
        profiles = beacon.beacon_list.get(user=user)
    except Profile.DoesNotExist:
        pass
    return profiles

def search(username):
    users = [user for user in User.objects.filter(username__startswith=username)]

    beacon_profiles = [get_beacon_profiles(user) for user in users if get_beacon_profiles(user) is not None]
    return beacon_profiles

s = search('davidjoy')
print(s)

