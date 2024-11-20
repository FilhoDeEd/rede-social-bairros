from account.serializers import AccountSerializer

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


# create account
    # name surname
    # birthday
    # username
    # email
    # password
    # agree_policy

    # checar se username é unique

    # checar se email é unique

    # Criar objeto Account e objeto Profile
        # Popular Account com as informações recebidas

class AccountRegisterView(APIView):
    def post(self, request):
        data = request.data
        user_data = request.data.get('user')
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=user_data['username'])
            user.set_password(user_data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'account': serializer.data})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountLoginView(APIView):
    """
    Handles user login requests.
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)


# Login
    # username
    # password

    # autenticar 
