from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def estudantes(request):
    estudantes={
        "id":1,
        "nome":"Lucas Marciano"
    }
    return JsonResponse(estudantes)