from django.test import TestCase
from apps.school.models import Estudante, Curso, Matricula

import datetime

# Create your tests here.

class test_EstudanteModelTestCase(TestCase):
    def setUp(self):
        cpf_student = "80597057095"
        self.course_id = "ABCDEF"
        Estudante.objects.create(
            nome = "Lucas Ioran Marciano",
            email = "l@l.com",
            cpf = cpf_student,
            data_nascimento = "1999-01-07",
            celular = "89 99999 9999"
        )

        Curso.objects.create(
            codigo = self.course_id,
            descricao = "Teste de criação de curso",
            nivel = "A"
        )

        self.enrollment = Matricula.objects.create(
            estudante = Estudante.objects.get(cpf=cpf_student),
            curso = Curso.objects.get(codigo=self.course_id),
            periodo = "N"
        )



    def test_assess_attributes_student(self):
        """Test attributes from student model"""
        estudante = Estudante.objects.get(email="l@l.com")
        self.assertEqual(estudante.nome, "Lucas Ioran Marciano")
        self.assertEqual(estudante.email, "l@l.com")
        self.assertEqual(estudante.cpf, "80597057095")
        self.assertEqual(estudante.data_nascimento, datetime.date(1999, 1, 7))
        self.assertEqual(estudante.celular, "89 99999 9999")
    
    def test_assess_attributes_course(self): 
        course = Curso.objects.get(codigo="ABCDEF")
        self.assertEqual(course.codigo, "ABCDEF")
        self.assertEqual(course.descricao, "Teste de criação de curso")
        self.assertEqual(course.nivel, "A")

    def test_assess_attributes_enrollment(self):
        self.assertEqual(self.enrollment.estudante, Estudante.objects.get(nome="Lucas Ioran Marciano"))
        self.assertEqual(self.enrollment.curso, Curso.objects.get(codigo=self.course_id))
        self.assertEqual(self.enrollment.periodo, "N")
