#encoding:utf-8
from django.forms import ModelForm
from school.models import Jornada,ProgramasAcademico

class JornadaForm(ModelForm):
    class Meta:
        model = Jornada
        # fields = ['name', 'description', 'is_active']

class PAcademicoForm(ModelForm):
    class Meta:
		model = ProgramasAcademico
        # fields = ['name', 'description', 'is_active']
