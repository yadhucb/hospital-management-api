from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'mobile',
            'password'
            ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)