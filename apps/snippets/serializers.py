from rest_framework import serializers
from apps.snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth import models

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_last_login = serializers.ReadOnlyField(source='owner.last_login')
    highlighted_code = serializers.HyperlinkedIdentityField(view_name='snippet-highlight') # view_name = [model]-[functions name with @action decorator]
    class Meta:
        model = Snippet
        exclude = ['highlighted']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    related_snippets = serializers.HyperlinkedIdentityField(many=True, view_name='snippet-detail', read_only=True)
    class Meta:
        model = models.User
        fields = ['id', 'username', 'related_snippets', 'url'] # 'related_snippets' because I specify related_name='related_snippets' 