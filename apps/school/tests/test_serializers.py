from django.test import TestCase
from apps.school.serializers import EstudanteSerializer
from apps.school.models import Estudante


class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = "Lucas Ioran Marciano",
            email = "l@l.com",
            cpf = "80597057095",
            data_nascimento = "1999-01-07",
            celular = "89 99999 9999"
        )
        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)

    def test_fields_student_serializer(self):
        self.assertEqual(set(self.serializer_estudante.data.keys()), set(['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']))