from django.contrib import admin

from apps.school.models import Estudante, Curso

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
    pass

admin.site.register(Curso, CursoAdmin)