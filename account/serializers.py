from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Profile
from beacon.models import Beacon
from utils.token import create_token


class AuthSerializer(serializers.Serializer):
    
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]


class TokenAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class RegisterUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    def create(self, validated_data):
        password = validated_data.get('password', '')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        profile = Profile.object.create(user=user)
        profile.save()
        Beacon.objects.create(user_profile=profile).save()
        return user
    
    def validate(self, data):
        password = data.get('password', '')
        user = User.objects.create(**data)
        user.set_password(password)
        user.full_clean()
        return data
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username, password, email']

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.CharField()
    
    class Meta:
        model = Profile
        fields = '__all__'