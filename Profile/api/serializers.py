from dataclasses import fields
from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')