from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.snippets import views 

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)