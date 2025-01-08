from django.contrib import admin

from apps.school.models import Estudante, Curso, Matricula

# Register your models here.

class EstudanteAdmin(admin.ModelAdmin):
    empty_value_display = "-?-"
    list_display  = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']
    list_display_links = ['id', 'nome']
    list_editable = ['celular']
    list_per_page = 20
    search_fields = ['nome']

admin.site.register(Estudante, EstudanteAdmin)

class CursoAdmin(admin.ModelAdmin):
    empty_value_display = "-?-"
    list_display  = ['id', 'codigo', 'descricao', 'nivel']
    list_display_links = ['id', 'codigo']
    list_editable = ['nivel']
    list_filter = ['nivel']
    list_per_page = 20
    search_fields = ['codigo']

admin.site.register(Curso, CursoAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    list_display  = ['id', 'estudante', 'curso', 'periodo']
    list_display_links = ['id', 'estudante', 'curso']
    list_filter = ['periodo']
    list_per_page = 20

admin.site.register(Matricula, MatriculaAdmin)