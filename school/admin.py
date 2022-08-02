from django.contrib import admin
from school.models import Jornada,ProgramasAcademico

class JornadaAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'date_added', 'is_active']

class ProgramasAcademicoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'description', 'activo', 'id_jornada']

admin.site.register(Jornada, JornadaAdmin)
admin.site.register(ProgramasAcademico, ProgramasAcademicoAdmin)
