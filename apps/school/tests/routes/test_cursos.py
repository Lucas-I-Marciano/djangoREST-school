from django.contrib.auth.models import User

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from apps.school.models import Curso

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
        self.assertEqual(Curso.objects.get().codigo, data["codigo"])

    def test_delete_course(self):
        data = {
            "codigo": "JS2",
            "descricao": "JavaScript2",
            "nivel": "B"
        }
        self.client.force_authenticate(self.superuser)
        response = self.client.post(self.url_list_course, data, format='json')
        url_delete = f'{self.url_list_course}{response.data['id']}/'
        response = self.client.delete(url_delete)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_course(self):
        data = {
            "codigo": "JS2",
            "descricao": "JavaScript2",
            "nivel": "B"
        }
        self.client.force_authenticate(self.superuser)
        response = self.client.post(self.url_list_course, data, format='json')
        url_update = f'{self.url_list_course}{response.data['id']}/' #/estudantes/1
        new_data = {**data}
        new_data['codigo'] = "JavaS2"
        response = self.client.put(url_update, new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)