from django.db import models
from django.contrib.auth.models import User


class Person(User):
    # beacon_list = models.ManyToManyField(User)
    is_panic = models.BooleanField(default=False)
    fake_pin = models.CharField(max_length=6)
    real_pin = models.CharField(max_length=6)