from typing import Dict
from account.serializers import AccountSerializer, UserSerializer

from django.contrib.auth import authenticate
from django.db import transaction

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from user_profile.serializers import UserProfileSerializer
from user_profile.models import Neighborhood, UserProfile


def add_errors(errors: Dict, serializer_errors: Dict):
    for field, error in serializer_errors.items():
        if field in errors:
            errors[field].extend(error)
        else:
            errors[field] = error


class RegisterView(APIView):
    """
    Handles user create account.
    """
    def post(self, request):
        data = request.data

        user_data = {
            'username': data.pop('username', ''),
            'password': data.pop('password', ''),
        }

        neighborhood_id = data.pop('neighborhood', '')

        user_serializer = UserSerializer(data=user_data)
        account_serializer = AccountSerializer(data=data)

        errors = {}

        if not user_serializer.is_valid():
            add_errors(errors=errors, serializer_errors=user_serializer.errors)

        if not account_serializer.is_valid():
            add_errors(errors=errors, serializer_errors=account_serializer.errors)
        
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            neighborhood = Neighborhood.objects.get(id=neighborhood_id)

            with transaction.atomic():
                user = user_serializer.save()
                account = account_serializer.save(user=user)
                UserProfile.objects.create(account=account, neighborhood=neighborhood)
                Token.objects.create(user=user)
        except Exception as e:
            return Response({'detail': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'detail': 'Success.'}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    """
    Handles user login requests.
    """
    def post(self, request):
        username = request.data.get('emailOrUsername')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'access': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
