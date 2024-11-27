from typing import Dict
from account.serializers import AccountSerializer, UserSerializer

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import transaction, IntegrityError

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


def add_errors(errors: Dict, serializer_errors: Dict):
    for field, error in serializer_errors.items():
        if field in errors:
            errors[field].extend(error)
        else:
            errors[field] = error


class AccountRegisterView(APIView):
    """
    Handles user create account.
    """
    def post(self, request):
        data = request.data

        user_data = {
            'username': data.pop('username', ''),
            'password': data.pop('password', ''),
        }

        profile_data = {
            'state': data.pop('state', ''),
            'city': data.pop('city', ''),
            'neighborhood': data.pop('neighborhood', ''),
        }

        user_serializer = UserSerializer(data=user_data)
        account_serializer = AccountSerializer(data=data)
        # profile_serializer = ProfileSerializer(data=profile_data)

        errors = {}

        # Validar cada serializer e acumular erros
        if not user_serializer.is_valid():
            add_errors(errors=errors, serializer_errors=user_serializer.errors)

        if not account_serializer.is_valid():
            add_errors(errors=errors, serializer_errors=account_serializer.errors)
        
        # if not profile_serializer.is_valid():
        #     add_errors(errors=errors, account_serializer=profile_serializer.errors)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                user = user_serializer.save()
                # user_profile = profile_serializer.save()
                account_serializer.save(user=user) #, active_user_profile=user_profile)
                Token.objects.create(user=user)
        except Exception as e:
            return Response({'detail': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'detail': 'Success.'}, status=status.HTTP_201_CREATED)


class AccountLoginView(APIView):
    """
    Handles user login requests.
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        account_serializer = AccountSerializer(user.account)
        # profile_serializer = UserProfileSerializer(user.account.active_user_profile)

        data = account_serializer
        # data |= profile_serializer

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'data': data}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
