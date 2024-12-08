from django.test import TestCase

from django.contrib.auth.models import User
from account.models import Profile
from .models import Beacon


david = User.objects.get(username='david')
david_profile = david.profile

david_joy = User.objects.get(username='davidjoy')
david_joy_profile = david_joy.profile

Beacon.sendPanic2Beacon(david)
beacon_profile = Beacon.getBeaconUser(david_profile)
print(beacon_profile)

Beacon.endPanic2Beacon(david)
beacon_profiles = Beacon.getBeaconUser(david_profile)
print(beacon_profiles)


beacons = Beacon.getBeacons(david_profile)
print(beacons)

for profile in beacons:
    panicing_user = profile.getUserInTerror()
    print(panicing_user)

beacon = Beacon.getBeaconUser(david_profile)
print(beacon)