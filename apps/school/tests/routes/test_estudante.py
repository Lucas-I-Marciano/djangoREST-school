from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from apps.school.models import Estudante

class test_EstudantesTestCase(APITestCase):
    fixtures = ["prototipo.json"]
    def setUp(self):
        self.estudante_1 = Estudante.objects.get(pk=1)
        

    def test_retrieve_student(self):
        self.assertEqual(self.estudante_1.cpf, '11111111111')