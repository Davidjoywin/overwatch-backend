from rest_framework import serializers

from .models import Beacon
from account.models import Profile

class BeaconSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beacon
        exclude = ['fake_pin', 'real_pin']

    def create(self, validated_data):
        is_valid = validated_data.get('is_panic', '')
        
        user = self.request.user
        profile = Profile.objects.get(user=user)
        beacon = Beacon.object.get(user=profile)
        beacon.is_panic = is_valid
        beacon.save()
        return beacon
    
    def validate(self, data):
        fake_pin = data.get('fake_pin', '')
        real_pin = data.get('real_pin', '')

        try:
            int(fake_pin) or int(real_pin)
        except ValueError:
            serializers.ValidationError({"Error": "pin should be convertable to an integer"})
        
        return data
