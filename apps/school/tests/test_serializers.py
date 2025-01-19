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
        self.assertEqual(self.serializer_estudante.data['nome'], self.estudante.nome)
        self.assertEqual(self.serializer_estudante.data['email'], self.estudante.email)
        self.assertEqual(self.serializer_estudante.data['cpf'], self.estudante.cpf)
        self.assertEqual(self.serializer_estudante.data['data_nascimento'], self.estudante.data_nascimento)
        self.assertEqual(self.serializer_estudante.data['celular'], self.estudante.celular)