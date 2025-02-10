from django.contrib.auth.models import User

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class test_CursosTestCase(APITestCase):
    def setUp(self):
        self.url_list_course = reverse('Cursos-list')
        self.superuser = User.objects.create_superuser("admin", "l@l.com", "test123")

    def test_list_course(self):
        self.client.force_authenticate(self.superuser)
        response = self.client.get(self.url_list_course)
        self.assertEqual(response.status_code, status.HTTP_200_OK)