from django.urls import path
from user_profile.views import (
    UFListAPIView,
    CityListAPIView,
    NeighborhoodListAPIView
)
from . import views

urlpatterns = [
    path('states/', UFListAPIView.as_view(), name='uf_list'),
    path('cities/<str:state_code>/', CityListAPIView.as_view(), name='city_list'),
    path('neighborhoods/<str:state_code>/<str:city_name>/', NeighborhoodListAPIView.as_view(), name='neighborhood_list'),
    path('', views.get_userProfiles)
]
