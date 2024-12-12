from django.shortcuts import get_object_or_404, render
from django.db import transaction
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from forum.serializers import ForumSerializer, ForumListSerializer
from account.views import add_errors
from forum.models import Forum , Subscriber 

from rest_framework import status
from rest_framework.response import Response

from user_profile.models import UserProfile


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
                account = request.user.account
                user_profile = UserProfile.objects.get(account=account, active=True)
                forum_serializer.save(owner=user_profile, neighborhood=user_profile.neighborhood)
        except Exception as e:
            return Response({'detail': f'An unexpected error occurred. {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'detail': 'Success.'}, status=status.HTTP_201_CREATED)


class ForumListView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ForumListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description']
    ordering_fields = ['subscribers_count', 'popularity', 'creation_date']
    ordering = ['-creation_date']

    def get_queryset(self):
        account = self.request.user.account
        
        try:
            user_profile = UserProfile.objects.get(account=account, active=True)
        except UserProfile.DoesNotExist:
            return Forum.objects.none()
        
        neighborhood = user_profile.neighborhood
        return Forum.objects.filter(neighborhood=neighborhood)


class ForumDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, slug):
        forum = get_object_or_404(Forum, slug=slug)
        serializer = ForumSerializer(forum)
        return Response(serializer.data, status=status.HTTP_200_OK)

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


class SubscribeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, forum_id):
        

        if not forum_id:
            return Response({'detail': 'Forum ID is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Obtém o fórum
            forum = Forum.objects.get(id=forum_id)
        except Forum.DoesNotExist:
            return Response({'detail': 'Forum not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            # Obtém o perfil do usuário autenticado
            account = request.user.account
            user_profile = UserProfile.objects.get(account=account, active=True)
        except UserProfile.DoesNotExist:
            return Response({'detail': 'Active user profile not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Verifica se o usuário já está inscrito no fórum
        if Subscriber.objects.filter(user_profile=user_profile, forum=forum).exists():
            return Response({'detail': 'User already subscribed to this forum.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                # Cria a inscrição
                Subscriber.objects.create(user_profile=user_profile, forum=forum)

                # Atualiza o contador de inscritos do fórum
                forum.subscribers_count += 1
                forum.save()

            return Response({'detail': 'Successfully subscribed to the forum.'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'detail': f'An error occurred: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
