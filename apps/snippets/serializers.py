from rest_framework import serializers
from apps.snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth import models

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    owner_last_login = serializers.ReadOnlyField(source='owner.last_login')
    class Meta:
        model = Snippet
        exclude = ['highlighted']


class UserSerializer(serializers.ModelSerializer):
    related_snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = models.User
        fields = ['id', 'username', 'related_snippets'] # 'related_snippets' because I specify related_name='related_snippets' 