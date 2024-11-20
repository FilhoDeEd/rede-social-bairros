from django.urls import path
from account.views import (
    AccountRegisterView,
    AccountLoginView
)

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),
    #path('logout', views.logout_view, name='logout')
]
