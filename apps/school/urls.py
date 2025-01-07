from django.urls import path
from apps.school.views import estudantes


urlpatterns = [
    path("", estudantes, name="estudantes"),
]