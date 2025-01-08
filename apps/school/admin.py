from django.contrib import admin

from apps.school.models import Estudante, Curso

# Register your models here.

class EstudanteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Estudante, EstudanteAdmin)

class CursoAdmin(admin.ModelAdmin):
    pass

admin.site.register(Curso, CursoAdmin)