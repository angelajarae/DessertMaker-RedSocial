from rest_framework import viewsets
from users import serializers
from users import models

# Create your views here.
class UserProfileView (viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()

class LikeView (viewsets.ModelViewSet):
    serializer_class=serializers.LikeSerializer
    queryset=models.Like.objects.all()

class SaveView (viewsets.ModelViewSet):
    serializer_class=serializers.SaveSerializer
    queryset=models.Save.objects.all()

class FollowerView (viewsets.ModelViewSet):
    serializer_class=serializers.FollowerSerializer
    queryset=models.Follower.objects.all()
