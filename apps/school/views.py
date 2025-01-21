from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, generics, filters

from apps.school.models import Estudante, Curso, Matricula
from apps.school.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, MatriculasEstudantesSerializer, MatriculasCursosSerializer, MatriculaSerializerV2

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.throttling import AnonRateThrottle
from apps.school.throttles import MatriculaRateThrottle

# Create your views here.

def estudantes(request):
    estudantes={
        "id":1,
        "nome":"Lucas Marciano"
    }
    return JsonResponse(estudantes)

class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de estudantes.

    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.

    Campos de pesquisa:
    - nome: permite pesquisar os resultados por nome.
    - cpf: permite pesquisar os resultados por CPF.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Classe de Serializer:
    - EstudanteSerializer: usado para serialização e desserialização de dados.
    - Se a versão da API for 'v2', usa EstudanteSerializerV2.
    """
    queryset = Estudante.objects.all().order_by('id')
    serializer_class = EstudanteSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']
    http_method_names = ["get", "post", "put"]

class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de cursos.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer
    http_method_names = ["get", "post", "put"]

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de matrículas.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """
    queryset = Matricula.objects.all().order_by('id')
    # serializer_class = MatriculaSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['curso__descricao'] # Performing a related lookup on a ForeignKey or ManyToManyField with the lookup API double-underscore notation
    throttle_classes = [AnonRateThrottle, MatriculaRateThrottle]
    http_method_names = ["get", "post", "put"]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return MatriculaSerializerV2
        return MatriculaSerializer


class MatriculasEstudantesView(generics.ListAPIView):
    """ 	
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    serializer_class = MatriculasEstudantesSerializer
    def get_queryset(self):
        return Matricula.objects.filter(estudante=self.kwargs['pk']).order_by('id')
    

class MatriculasCursosView(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """
    serializer_class = MatriculasCursosSerializer
    def get_queryset(self):
        return Matricula.objects.filter(curso=self.kwargs['pk']).order_by('id')