from django.db import models
from django.contrib.auth.models import User

from account.models import Profile


class Beacon(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    beacon_list = models.ManyToManyField(Profile, related_name='beacon_profile')
    is_panic = models.BooleanField(default=False)
    fake_pin = models.CharField(max_length=6)
    real_pin = models.CharField(max_length=6)

    def __str__(self):
        return f"Beacons for {self.user.user.username}"

    @classmethod
    def make_list_get_panic(cls, user):
        profile = Profile.objects.get(user=user)
        beacon = Beacon.objects.get(profile=profile)
        beacon_list = beacon.beacon_list.all()