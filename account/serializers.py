from django.contrib.auth.models import User

from rest_framework import serializers

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

    def create(self, validated_data):
        ...