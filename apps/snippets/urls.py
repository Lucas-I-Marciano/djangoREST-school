from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.snippets import views

from rest_framework import renderers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'snippets', views.SnippetViewSet, basename='snippetsss')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)