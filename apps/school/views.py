from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets

from apps.school.models import Estudante
from apps.school.serializers import EstudanteSerializer

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