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
    forum_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Forum
        fields = [
            'forum_id',
            'title',
            'description',
            'slug',
            'popularity'
        ]

class ForumEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = [
            'title',
            'description'
        ]