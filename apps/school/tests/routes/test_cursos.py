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

    def test_create_course_without_authentication(self):
        data = {
            "codigo": "JS2",
            "descricao": "JavaScript2",
            "nivel": "B"
        }
        response = self.client.post(self.url_list_course, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_course_with_authentication(self):
        data = {
            "codigo": "JS2",
            "descricao": "JavaScript2",
            "nivel": "B"
        }
        self.client.force_authenticate(self.superuser)
        response = self.client.post(self.url_list_course, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)