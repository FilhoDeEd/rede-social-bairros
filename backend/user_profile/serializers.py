from rest_framework import serializers
from user_profile.models import Neighborhood, UserProfile


class NeighborhoodSerializer(serializers.ModelSerializer):
    neighborhood = serializers.CharField(source='name')

    class Meta:
        model = Neighborhood
        fields = ['id', 'neighborhood', 'state', 'locality']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'trust_rate', 'active', 'status']
