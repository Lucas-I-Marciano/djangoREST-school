from django.http import Http404

from apps.snippets.models import Snippet
from apps.snippets.serializers import SnippetSerializer

from rest_framework import status, permissions, mixins, generics
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView




# Create your views here.
@permission_classes((permissions.AllowAny,))
class SnippetList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
    ):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@permission_classes((permissions.AllowAny,))
class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
