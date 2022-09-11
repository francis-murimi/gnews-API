from rest_framework import serializers
from django.contrib.auth.models import User # importing user model
from .models import UserProfile, PastorProfile, LeaderProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','first_name','last_name','gender','date_of_birth']

class PastorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastorProfile
        fields = ['id','first_name','last_name','gender','date_of_birth']

class LeaderProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderProfile
        fields = ['id','first_name','last_name','gender','date_of_birth']