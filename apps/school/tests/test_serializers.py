from django.test import TestCase
from apps.school.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializerV2
from apps.school.models import Estudante, Curso, Matricula
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

class SerializerCourseTestCase(TestCase):
    def setUp(self):
        self.curso = Curso(
            codigo = "ABCDEF",
            descricao = "Instância do curso de teste",
            nivel = "A"
        )
        self.serializer_course = CursoSerializer(instance=self.curso)
    
    def test_fields_course_serializer(self):
        set_data = set(self.serializer_course.data)
        set_serializer_course_fields = set([
            'codigo', 'descricao', 'nivel', 'id'
        ])
        self.assertEqual(set_data, set_serializer_course_fields)

    def test_field_value_course_serializer(self):
        data = self.serializer_course.data
        self.assertEqual(data['codigo'], self.curso.codigo)
        self.assertEqual(data['descricao'], self.curso.descricao)
        self.assertEqual(data['nivel'], self.curso.nivel)
        assert_dict = {
            "id": None,
            "codigo" : self.curso.codigo,
            "descricao" : self.curso.descricao,
            "nivel" : self.curso.nivel,
        }
        self.assertEqual(dict(data), assert_dict)


class SerializerEnrollmentTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = "Lucas Ioran Marciano",
            email = "l@l.com",
            cpf = "80597057095",
            data_nascimento = "1999-01-07",
            celular = "89 99999 9999"
        )
        self.curso = Curso(
            codigo = "ABCDEF",
            descricao = "Instância do curso de teste",
            nivel = "A"
        )
        self.matricula = Matricula(
            estudante = self.estudante,
            curso = self.curso,
            periodo = "M"
        )
        self.serializer_enrollment = MatriculaSerializerV2(instance=self.matricula)

    def test_fields_course_serializer(self):
        set_data = set(self.serializer_enrollment.data)
        set_fields = set(['id', 'estudante', 'curso', 'periodo'])
        self.assertEqual(set_data, set_fields)

    def test_field_value_enrollment_serializer(self):
        data = self.serializer_enrollment.data
        self.assertEqual(data['estudante'], self.estudante.nome) # Because on serializer: curso = serializers.ReadOnlyField(source='curso.descricao')
        self.assertEqual(data['curso'], self.curso.descricao) # Because on serializer: estudante = serializers.ReadOnlyField(source='estudante.nome')
        self.assertEqual(data['periodo'], 'Matutino') # Because on serializer: periodo = serializers.SerializerMethodField() --> obj.get_periodo_display()