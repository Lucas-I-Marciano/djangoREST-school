from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.snippets import views

user_list = views.UserViewSet.as_view({
    'get':'list'
})

user_detail = views.UserViewSet.as_view({
    'get' : 'retrieve',
})

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

urlpatterns = [
    path('snippets/', snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight')
]

urlpatterns = format_suffix_patterns(urlpatterns)