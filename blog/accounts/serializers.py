from rest_framework import serializers
from models import UserProfile

# App imports
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'location', 'about_me')


