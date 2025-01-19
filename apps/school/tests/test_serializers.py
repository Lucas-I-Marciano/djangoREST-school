from django.test import TestCase
from apps.school.serializers import EstudanteSerializer
from apps.school.models import Estudante
from datetime import date


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

    def test_field_value_student_serializer(self):
        self.assertEqual(self.serializer_estudante.data['nome'], "Lucas Ioran Marciano")
        self.assertEqual(self.serializer_estudante.data['email'], "l@l.com")
        self.assertEqual(self.serializer_estudante.data['cpf'], "80597057095")
        self.assertEqual(self.serializer_estudante.data['data_nascimento'], "1999-01-07")
        self.assertEqual(self.serializer_estudante.data['celular'], "89 99999 9999")