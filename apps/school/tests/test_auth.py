from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class test_AutenticacaoUsuario(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser("admin", "l@l.com", "test123")

    def test_correct_authentication(self):
        user = authenticate(username="admin", password="test123")
        is_user_authenticated = (user.is_authenticated) and (user is not None)
        self.assertTrue(is_user_authenticated)

    def test_wrong_username_authentication(self):
        user = authenticate(username="Admin", password="test123")
        if user is None:
            is_user_authenticated = False
        else:
            is_user_authenticated = (user.is_authenticated) and (user is not None)
        self.assertFalse(is_user_authenticated)

    def test_wrong_password_authentication(self):
        user = authenticate(username="admin", password="test1234")
        if user is None:
            is_user_authenticated = False
        else:
            is_user_authenticated = (user.is_authenticated) and (user is not None)
        self.assertFalse(is_user_authenticated)
    