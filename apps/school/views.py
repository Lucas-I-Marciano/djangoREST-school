from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, generics

from apps.school.models import Estudante, Curso, Matricula
from apps.school.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, MatriculasEstudantesSerializer

# Create your views here.

def estudantes(request):
    estudantes={
        "id":1,
        "nome":"Lucas Marciano"
    }
    return JsonResponse(estudantes)

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class MatriculasEstudantesView(generics.ListAPIView):
    serializer_class = MatriculasEstudantesSerializer
    def get_queryset(self):
        return Matricula.objects.filter(estudante=self.kwargs['pk'])