from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from user_profile.models import Neighborhood, UfChoices


class UFListAPIView(APIView):
    """
    Returns the list of all Brazilian states (UFs).
    """
    def get(self, request, *args, **kwargs):
        ufs = [{'code': uf.value, 'name': uf.label} for uf in UfChoices]
        return Response(ufs, status=HTTP_200_OK)


class CityListAPIView(ListAPIView):
    """
    Returns all cities for a given state.
    """
    def get(self, request, state_code, *args, **kwargs):
        if state_code not in UfChoices.values:
            raise NotFound(f"State '{state_code}' not found.")

        cities = Neighborhood.objects.filter(state=state_code).values_list('locality', flat=True).distinct()
        return Response(list(cities), status=HTTP_200_OK)


class NeighborhoodListAPIView(ListAPIView):
    """
    Returns all neighborhoods for a specific city in a given state.
    """
    def get(self, request, state_code, city_name, *args, **kwargs):
        if state_code not in UfChoices.values:
            raise NotFound(f"State {state_code} not found.")

        neighborhoods = Neighborhood.objects.filter(state=state_code, locality=city_name).values_list('name', flat=True)
        if not neighborhoods.exists():
            raise NotFound(f"No neighborhoods found for city '{city_name}' in state '{state_code}'.")

        return Response(list(neighborhoods), status=HTTP_200_OK)
