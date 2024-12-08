from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_panic = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    @classmethod
    def getProfile(cls, user):
        try:
            profile = cls.objects.get(user=user)
            return profile
        except cls.DoesNotExist:
            return None

    def getUserInTerror(self):
        panicing_user = self.beacon_profile.all()
        return panicing_user
