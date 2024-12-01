from django.urls import path
from account.views import (
    RegisterView,
    LoginView,
    DetailAccountView,
)


urlpatterns = [
    path('detail/', DetailAccountView.as_view(), name='account_detail'),
    path('register/', RegisterView.as_view(), name='account_register'),
    path('login/', LoginView.as_view(), name='account_login'),
]
