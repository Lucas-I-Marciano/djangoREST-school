from django.urls import path
from apps.school.views import estudantes

from rest_framework import routers

from apps.school.views import EstudanteViewSet

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet)

urlpatterns = router.urls