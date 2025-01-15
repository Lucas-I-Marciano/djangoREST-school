from rest_framework import serializers
from apps.school.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    
    def validate(self, data):
        if not data['nome'].replace(' ', '').isalpha():
            raise serializers.ValidationError({"nome":"Nome inválido"})
        if len(data['cpf']) != 11:
            raise serializers.ValidationError({"cpf":"CPF Inválido"})
        if len(data['celular']) != 13:
            raise serializers.ValidationError({"celular":"Celular Inválido"})
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