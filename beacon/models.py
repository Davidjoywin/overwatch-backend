from django.db import models
from django.contrib.auth.models import User

from account.models import Profile


class Beacon:...

class Beacon(models.Model):
    user = models.ForeignKey(Profile, blank=True, on_delete=models.CASCADE)
    beacon_list = models.ManyToManyField(Profile, related_name='beacon_profile', blank=True)
    is_panic = models.BooleanField(default=False)
    fake_pin = models.CharField(max_length=6, blank=True)
    real_pin = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return f"Beacons for {self.user.user.username}"

    @classmethod
    def sendPanic2Beacon(cls, user) -> None:
        profile = Profile.objects.get(user=user)
        beacon = cls.objects.get(user=profile)
        beacon._setPanic(p_val=True)

    @classmethod
    def endPanic2Beacon(cls, user) -> None:
        profile = Profile.objects.get(user=user)
        beacon = cls.objects.get(user=profile)
        beacon._setPanic(p_val=False)

    def _setPanic(self, p_val: bool) -> None:
        self.is_panic = p_val
        self.save()

    @classmethod
    def getBeaconProfiles(cls, profile)-> list:
        # get list of profiles that will receive panic alarm
        beacon = cls.objects.get(user=profile)
        profiles = [beacon for beacon in beacon.beacon_list.all()]
        return profiles
    
    @classmethod
    def getBeaconUser(cls, user_profile) -> Beacon:
        # get who is sending for help
        beacon_profile = cls.objects.get(user=user_profile)
        return beacon_profile
