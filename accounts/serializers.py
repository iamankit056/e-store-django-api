from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Address,
    Profile
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, data):
        return User.objects.create_user(**data)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ('id', )


class ProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    user = UserSerializer()    
    class Meta:
        model = Profile
        fields = '__all__'


class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()


class UploadAvtarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avtar',)