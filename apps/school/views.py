from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, generics

from apps.school.models import Estudante, Curso, Matricula
from apps.school.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, MatriculasEstudantesSerializer, MatriculasCursosSerializer

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def estudantes(request):
    estudantes={
        "id":1,
        "nome":"Lucas Marciano"
    }
    return JsonResponse(estudantes)

class EstudanteViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class MatriculasEstudantesView(generics.ListAPIView):
    serializer_class = MatriculasEstudantesSerializer
    def get_queryset(self):
        return Matricula.objects.filter(estudante=self.kwargs['pk'])
    

class MatriculasCursosView(generics.ListAPIView):
    serializer_class = MatriculasCursosSerializer
    def get_queryset(self):
        return Matricula.objects.filter(curso=self.kwargs['pk'])