from django.contrib import admin

from apps.school.models import Estudante

# Register your models here.

class EstudanteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Estudante, EstudanteAdmin)