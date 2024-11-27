from django.shortcuts import render
from django.db import transaction
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from forum.serializers import ForumSerializer, ForumListSerializer
from account.views import add_errors
from forum.models import Forum

from rest_framework import status
from rest_framework.response import Response


class ForumRegisterView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data

        forum_serializer = ForumSerializer(data=data)

        errors = {}

        if not forum_serializer.is_valid():
            add_errors(errors=errors, serializer_errors=forum_serializer.errors)

        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            with transaction.atomic():
                user_profile = request.user.account.active_user_profile
                forum = forum_serializer.save(owner=user_profile, neighboorhood=user_profile.neighboorhood)
        except Exception as e:
            return Response({'detail': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'detail': 'Success.'}, status=status.HTTP_201_CREATED)


class ForumListView(ListAPIView):
    queryset = Forum.objects.all()  # Define o queryset base
    serializer_class = ForumListSerializer
    filter_backends = [SearchFilter, OrderingFilter]  # Adiciona filtros de busca e ordenação
    search_fields = ['title', 'description']  # Campos para busca (e.g., name contains value)
    ordering_fields = ['subscribers_count', 'popularity', 'creation_date']  # Ordenação permitida
    ordering = ['-creation_date']  # Ordenação padrão (mais recentes primeiro)


# Listar os foruns (o sistema de busca já vem aqui) (retornar dados simples de vários foruns)
    # Há um queryset de foruns
    # O front deve pedir partes desse queryset
        # Pode pedir um range de objetos (1 a 10, 11 a 20 e etc) ou aplicar um filtro (name contains value, numero de inscritos e etc)
        # pode ser um paginate (page 1 -> 0 a 29; page 2 -> 30 a 59 e assim vai) (aí recebe a page como argumento)
    # Deve ter algo pronto para paginação
    # Um serializer para as informações básicas (serializer queryset -> many=True)
    # Funciona para o infinit scroll ou para o paginas estáticas

# Detalhar o forum (retorna os dados de um forum)
    # Possivelmente irá utilizar o mesmo serializer do criar forum


# Atualizar os dados do forum (acho que n precisa ser por agr)

# Excluir forum (acho que n precisa ser por agr tbm)


