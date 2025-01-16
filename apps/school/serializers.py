from rest_framework import serializers
from apps.school.models import Estudante, Curso, Matricula
from apps.school.validators import nome_invalido, cpf_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    
    def validate(self, data):
        if nome_invalido(data['nome']):
            raise serializers.ValidationError({"nome":"Nome inválido"})
        if cpf_invalido(data['cpf']):
            raise serializers.ValidationError({"cpf":"CPF Inválido"})
        if celular_invalido(data['celular']):
            raise serializers.ValidationError({"celular":"Celular deve seguir padrão: 89 99999-9999"})
        return data


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class MatriculasEstudantesSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta :
        model = Matricula
        fields = ['id', 'curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class MatriculasCursosSerializer(serializers.ModelSerializer):
    periodo = serializers.SerializerMethodField()
    estudante = serializers.ReadOnlyField(source='estudante.nome')
    estudante_email = serializers.ReadOnlyField(source='estudante.email')
    class Meta:
        model = Matricula
        fields = ['id', 'periodo', 'estudante', 'estudante_email']

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class MatriculaSerializerV2(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    estudante = serializers.ReadOnlyField(source='estudante.nome')
    
    periodo = serializers.SerializerMethodField()
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    class Meta:
        model = Matricula
        exclude = []