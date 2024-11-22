from account.models import Account
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


class EmailOrUsernameBackend(BaseBackend):
    """
    Custom authentication backend to allow login using either email (from Account) or username.
    """

    def authenticate(self, request, username=None, password=None):
        email_validator = EmailValidator()
        user = None

        try:
            email_validator(username)
            account = Account.objects.get(email=username)
            user = account.user
        except ValidationError:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None
        except Account.DoesNotExist:
            return None

        if user and user.check_password(password):
            return user

        return None

    def get_user(self, user_id):
        """
        Retorna um usuário baseado no ID.
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
