from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )