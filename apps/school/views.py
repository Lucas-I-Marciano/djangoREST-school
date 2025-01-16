from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, generics, filters

from apps.school.models import Estudante, Curso, Matricula
from apps.school.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, MatriculasEstudantesSerializer, MatriculasCursosSerializer, MatriculaSerializerV2

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

def estudantes(request):
    estudantes={
        "id":1,
        "nome":"Lucas Marciano"
    }
    return JsonResponse(estudantes)

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by('id')
    serializer_class = EstudanteSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by('id')
    # serializer_class = MatriculaSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['curso__descricao'] # Performing a related lookup on a ForeignKey or ManyToManyField with the lookup API double-underscore notation

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return MatriculaSerializerV2
        return MatriculaSerializer


class MatriculasEstudantesView(generics.ListAPIView):
    serializer_class = MatriculasEstudantesSerializer
    def get_queryset(self):
        return Matricula.objects.filter(estudante=self.kwargs['pk']).order_by('id')
    

class MatriculasCursosView(generics.ListAPIView):
    serializer_class = MatriculasCursosSerializer
    def get_queryset(self):
        return Matricula.objects.filter(curso=self.kwargs['pk']).order_by('id')