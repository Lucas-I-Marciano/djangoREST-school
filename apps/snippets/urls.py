from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.snippets import views

from rest_framework import renderers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')

snippet_list = views.SnippetViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

snippet_detail = views.SnippetViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

urlpatterns = [
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('', include(router.urls)),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight')
]

# urlpatterns = format_suffix_patterns(urlpatterns)