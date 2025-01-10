from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from apps.snippets.models import Snippet
from apps.snippets.serializers import SnippetSerializer

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.views import APIView

# Create your views here.
@permission_classes((permissions.AllowAny,))
class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def snippet_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try :
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)