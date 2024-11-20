from account.models import Account
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.db import transaction, IntegrityError
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ['user', 'name', 'surname', 'birthday', 'email', 'agree_policy']

    def validate(self, data):
        if not data.get('agree_policy', False):
            raise serializers.ValidationError({'agree_policy': 'You must agree to the terms and conditions.'})

        return data

    def create(self, validated_data):
        user_data = validated_data.get('user')

        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user = user_serializer.save()

            account = Account.objects.create(
                user=user,
                name=validated_data['name'],
                surname=validated_data['surname'],
                email=validated_data['email'],
                birthday=validated_data['birthday'],
                agree_policy=validated_data['agree_policy'],
            )

            return account
        else:
            raise serializers.ValidationError(user_serializer.errors)

# class AccountSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(write_only=True)  # Campo extra para confirmação de senha
#     password = serializers.CharField(write_only=True)  # A senha para criação do usuário

#     class Meta:
#         model = Account
#         fields = [
#             'name',
#             'surname',
#             'birthday',
#             'username',  # Este campo é do modelo User
#             'email',
#             'password',
#             'confirm_password',
#             'agree_policy',
#         ]
#         extra_kwargs = {
#             'password': {'write_only': True},  # Senha não será retornada
#             'agree_policy': {'write_only': True},  # Campo para aceitar os termos
#         }

#     def validate(self, data):
#         # Verifica se as senhas coincidem
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError({'password': 'Passwords do not match.'})

#         # Validação de email
#         email_validator = EmailValidator()
#         try:
#             email_validator(data['email'])
#         except Exception:
#             raise serializers.ValidationError({'email': 'Invalid email format.'})

#         # Verifica se o usuário concordou com os termos
#         if not data.get('agree_policy', False):
#             raise serializers.ValidationError({'agree_policy': 'You must agree to the terms and conditions.'})

#         return data

#     def create(self, validated_data):
#         # Remove a confirmação da senha, pois não deve ser salva no banco de dados
#         validated_data.pop('confirm_password', None)

#         try:
#             with transaction.atomic():
#                 # Criação do usuário
#                 user = User.objects.create_user(
#                     username=validated_data['username'],  # Cria o usuário com o username
#                     password=validated_data['password'],  # A senha do usuário
#                 )

#                 # Criação da conta associada ao usuário
#                 account = Account.objects.create(
#                     user=user,
#                     name=validated_data['name'],
#                     surname=validated_data['surname'],
#                     email=validated_data['email'],
#                     birthday=validated_data['birthday'],
#                     agree_policy=validated_data['agree_policy'],
#                 )

#                 return account

#         except IntegrityError as e:
#             if 'unique constraint' in str(e).lower():
#                 if 'username' in str(e):
#                     raise serializers.ValidationError({'username': 'Username is already taken.'})
#                 elif 'email' in str(e):
#                     raise serializers.ValidationError({'email': 'Email is already in use.'})
#             raise serializers.ValidationError({'detail': 'An error occurred while creating the account.'})
