#encoding:utf-8
from django.forms import ModelForm
from school.models import Jornada,ProgramasAcademico

class JornadaForm(ModelForm):
    class Meta:
        model = Jornada
        fields = ['name', 'description']

class PAcademicoForm(ModelForm):
    class Meta:
        model = ProgramasAcademico
        fields = ['nombre', 'description']
