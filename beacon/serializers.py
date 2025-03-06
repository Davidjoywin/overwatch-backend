from rest_framework import serializers

from .models import Beacon
from account.models import Profile

class BeaconSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beacon
        fields = "__all__"
        # exclude = ['fake_pin', 'real_pin']

    def create(self, validated_data):
        # is_panic = validated_data.get('is_panic', False)
        
        # user = self.request.user
        # profile = Profile.objects.get(user=user)
        # beacon = Beacon.object.get(user=profile)
        # beacon.is_panic = is_panic
        # beacon.save()
        beacon = Beacon.objects.create(**validated_data)
        beacon.save()
        return beacon
    
    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        return instance
    
    def validate(self, data):
        fake_pin = data.get('fake_pin', '')
        real_pin = data.get('real_pin', '')

        try:
            int(fake_pin)
            int(real_pin)
        except ValueError:
            serializers.ValidationError({"Error": "pin should be convertible to an integer"})
        return data
    

class SecuritySerializer(serializers.Serializer):
    # works with the Profile model
    real_pin = serializers.CharField()
    fake_pin = serializers.CharField()

    def update(self, instance, validated_data):
        fake_pin = validated_data.get("fake_pin", instance.fake_pin)
        real_pin = validated_data.get("real_pin", instance.real_pin)
        # assign conditionally if the data assigned is empty,
        # then just give it back it own instance value
        instance.fake_pin = fake_pin
        instance.real_pin = real_pin
        instance.save()
        return instance

    def validate(self, data):
        fake_pin = data.get("fake_pin", '')
        real_pin = data.get("real_pin", '')
        try:
            int(fake_pin)
            int(real_pin)
        except Exception:
            serializers.ValidationError({"Error": "pin should be convertible to an integer"})
        return data

# class GlobalBeacon(serializers.Serializer):
#     def create(self, validated_data):
#         is
