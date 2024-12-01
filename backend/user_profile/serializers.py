from rest_framework import serializers
from user_profile.models import Neighborhood, UserProfile


class NeighborhoodSerializer(serializers.ModelSerializer):
    neighborhood_id = serializers.IntegerField(source='id', read_only=True)
    neighborhood = serializers.CharField(source='name')

    class Meta:
        model = Neighborhood
        fields = ['neighborhood_id', 'neighborhood', 'state', 'locality']


class UserProfileSerializer(serializers.ModelSerializer):
    user_profile_id = serializers.IntegerField(source='id', read_only=True)
    status = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user_profile_id', 'trust_rate', 'active', 'status']
