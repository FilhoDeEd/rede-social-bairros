from account.models import Account
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class AccountSerializer(serializers.ModelSerializer):
    account_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = Account
        fields = ['account_id', 'name', 'surname', 'gender', 'birthday', 'email', 'cellphone', 'agree_policy', 'biography']

    def validate_agree_policy(self, value):
        if not value:
            raise serializers.ValidationError('Agree to the terms and conditions.')
        return value


class UpdateAccountBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name', 'surname', 'gender', 'birthday', 'cellphone', 'biography']
