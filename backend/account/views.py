from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


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

class LoginView(APIView):
    """
    Handles user login requests.
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# Login
    # username
    # password

    # autenticar 
