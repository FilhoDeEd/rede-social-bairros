from forum.models import Forum
from rest_framework import serializers


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = [
            'id',
            'title',
            'slug',
            'description',
            'subscribers_count',
            'popularity',
            'creation_date',
            'update_date'
        ]
        read_only_fields = ['id', 'slug', 'creation_date', 'update_date', 'subscribers_count', 'popularity']


class ForumListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = [
            'id',
            'title',
            'description',
            'slug',
            'popularity'
        ]
