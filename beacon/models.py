from django.db import models
from django.contrib.auth.models import User

from account.models import Profile


class Beacon(models.Model):
    user_profile = models.ForeignKey(Profile, blank=True, on_delete=models.CASCADE)
    beacon_list = models.ManyToManyField(Profile, related_name='list_beacon_profiles', blank=True)
    is_panic = models.BooleanField(default=False)
    beacon_origin = models.JSONField(blank=True, null=True)
    beacon_movement = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Beacons for {self.user_profile.user.username}"
    
    def _setPanic(self, p_val: bool) -> None:
        self.is_panic = p_val
        self.save()

    @classmethod
    def sendPanic2Beacon(cls, user) -> None:
        profile = Profile.objects.get(user=user)
        beacon = cls.objects.get(user_profile=profile)
        beacon._setPanic(p_val=True)

    @classmethod
    def getBeaconFromProfile(cls, user) -> None:
        # notify user's friends about a user beacon
        beacons = Beacon.objects.filter(beacon_list__user__username=user.username)
        user_beacons = [beacon for beacon in beacons]
        return user_beacons

    @classmethod
    def endPanic2Beacon(cls, user) -> None:
        profile = Profile.objects.get(user=user)
        beacon = cls.objects.get(user_profile=profile)
        beacon._setPanic(p_val=False)

    @classmethod
    def getBeaconableProfiles(cls, profile)-> list:
        # get list of profiles that will receive panic alarm
        beacon = cls.objects.get(user_profile=profile)
        profiles = [beacon for beacon in beacon.beacon_list.all()]
        return profiles
    
    @classmethod
    def getBeaconUser(cls, user_profile) -> any:
        # get who is sending for help
        beacon_profile = cls.objects.get(user_profile=user_profile)
        return beacon_profile
