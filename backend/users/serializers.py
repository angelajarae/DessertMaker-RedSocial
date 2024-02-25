from rest_framework import serializers
from users import models

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.UserProfile
        fields="__all__"

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Like
        fields="__all__"

class SaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Save
        fields="__all__"

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Follower
        fields="__all__"