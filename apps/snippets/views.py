from django.http import Http404
from django.contrib.auth.models import User

from apps.snippets.models import Snippet
from apps.snippets.serializers import SnippetSerializer, UserSerializer

from rest_framework import status, permissions, mixins, generics, renderers
from rest_framework.decorators import permission_classes, api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.snippets.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse

from rest_framework import viewsets



# Create your views here.

class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]