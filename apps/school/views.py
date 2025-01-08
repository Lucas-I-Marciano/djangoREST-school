from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets

from apps.school.models import Estudante, Curso
from apps.school.serializers import EstudanteSerializer, CursoSerializer

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