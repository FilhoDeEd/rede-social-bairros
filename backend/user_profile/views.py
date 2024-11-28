from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user_profile.models import Neighborhood, UfChoices, UserProfile
from rest_framework.decorators import api_view
import json

from .serializers import UserProfileSerializer

class UFListAPIView(APIView):
    """
    Returns the list of all Brazilian states (UFs).
    """
    def get(self, request, *args, **kwargs):
        ufs = [{'code': uf.value, 'name': uf.label} for uf in UfChoices]
        return Response(ufs, status=status.HTTP_200_OK)


class CityListAPIView(ListAPIView):
    """
    Returns all cities for a given state.
    """
    def get(self, request, state_code, *args, **kwargs):
        if state_code not in UfChoices.values:
            raise NotFound(f"State '{state_code}' not found.")

        cities_list = Neighborhood.objects.filter(state=state_code).values_list('locality', flat=True).distinct()
        cities = [{'name': city} for city in cities_list]

        return Response(cities, status=status.HTTP_200_OK)


class NeighborhoodListAPIView(ListAPIView):
    """
    Returns all neighborhoods for a specific city in a given state.
    """
    def get(self, request, state_code, city_name, *args, **kwargs):
        if state_code not in UfChoices.values:
            raise NotFound(f"State {state_code} not found.")

        neighborhoods_list = Neighborhood.objects.filter(state=state_code, locality=city_name).values_list('name', flat=True)
        if not neighborhoods_list.exists():
            raise NotFound(f"No neighborhoods found for city '{city_name}' in state '{state_code}'.")
        
        neighborhoods = [{'name': neighborhoods} for neighborhoods in neighborhoods_list]


        return Response(neighborhoods, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_userProfiles(request):
    if request.method == 'GET':
        username = request.query_params.get('username')  
        
        if not username:
            return Response(
                {"error": "Username parameter is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user_profile = UserProfile.objects.get(username=username)  
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data)
        except UserProfile.DoesNotExist:
            return Response(
                {"error": "UserProfile not found."},
                status=status.HTTP_404_NOT_FOUND
            )
            