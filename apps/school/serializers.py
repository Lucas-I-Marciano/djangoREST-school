from rest_framework import serializers
from apps.school.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

    def validate_nome(self, value):
        """Check that 'nome' field is alphabetical

        Args:
            value (str): name value

        Returns:
            value: If validation is ok
            raise Error: If validation is NOT ok
        """
        if not value.replace(' ', '').isalpha() :
            raise serializers.ValidationError("Nome inválido")
        return value


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