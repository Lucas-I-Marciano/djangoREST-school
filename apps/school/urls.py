from django.urls import path, include
from apps.school.views import estudantes

from rest_framework import routers

from apps.school.views import EstudanteViewSet, CursoViewSet

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet)
router.register('cursos', CursoViewSet, basename="Cursos")

urlpatterns = [
    path('', include(router.urls))
]