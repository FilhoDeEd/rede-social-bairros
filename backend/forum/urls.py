from django.urls import path
from forum.views import (
    ForumRegisterView,
    ForumListView
)


urlpatterns = [
    path('register/',ForumRegisterView.as_view(), name='forum_register'),
    path('list/', ForumListView.as_view(), name='forum_list')
]
