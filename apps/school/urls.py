from django.urls import path, include
from apps.school.views import estudantes

from rest_framework import routers

from apps.school.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, MatriculasEstudantesView, MatriculasCursosView
from apps.snippets import views

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet)
router.register('cursos', CursoViewSet, basename="Cursos")
router.register('matriculas', MatriculaViewSet, basename="Matriculas")
router.register('users', views.UserViewSet, basename='user')
router.register('snippets', views.SnippetViewSet, basename='snippet')

urlpatterns = [
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', MatriculasEstudantesView.as_view()),
    path('cursos/<int:pk>/matriculas/', MatriculasCursosView.as_view()),
]