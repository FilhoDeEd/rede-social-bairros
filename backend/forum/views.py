from django.shortcuts import get_object_or_404, render
from django.db import transaction
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from forum.serializers import ForumSerializer, ForumListSerializer, ForumEditSerializer
from account.views import add_errors
from forum.models import Forum , Subscriber 
from django.utils.text import slugify


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
                forum = forum_serializer.save(owner=user_profile, neighborhood=user_profile.neighborhood)
        except Exception as e:
            return Response({'detail': f'An unexpected error occurred. {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({'detail': 'Success.', 'slug': forum.slug}, status=status.HTTP_201_CREATED)


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


class ForumEditView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        # Obtém o fórum pelo slug
        forum = get_object_or_404(Forum, slug=slug)

        account = self.request.user.account

        try:
            user_profile = UserProfile.objects.get(account=account, active=True)
        except UserProfile.DoesNotExist:
            return Response({"detail": "Invalid or inactive user."}, status=status.HTTP_400_BAD_REQUEST)

        # Verifica se o usuário logado é o dono do fórum
        if forum.owner != user_profile:
            return Response({"detail": "You do not have permission to edit this forum."}, status=status.HTTP_403_FORBIDDEN)

        # Atualiza os dados e ajusta o slug com base no título
        forum_serializer = ForumEditSerializer(forum, data=request.data)
        if forum_serializer.is_valid():
            forum = forum_serializer.save()  # Salva os dados validados
            # Atualiza o slug com base no novo título
            forum.slug = slugify(forum.title)
            forum.save()
            return Response({"success": "success"}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": forum_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




class ForumDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, slug):
        # Obtém o fórum pelo slug
        forum = get_object_or_404(Forum, slug=slug)

        # Obtém a conta do usuário logado
        account = self.request.user.account
        
        try:
            user_profile = UserProfile.objects.get(account=account, active=True)
        except UserProfile.DoesNotExist:
            return Response({"detail": "Perfil de usuário ativo não encontrado."}, status=status.HTTP_400_BAD_REQUEST)

        # Verifica se o usuário logado é o dono do fórum
        if forum.owner != user_profile:
            return Response({"detail": "Você não tem permissão para excluir este fórum."}, status=status.HTTP_403_FORBIDDEN)

        # Deleta o fórum
        forum.delete()

        return Response({"detail": "Fórum excluído com sucesso."}, status=status.HTTP_200_OK)


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
