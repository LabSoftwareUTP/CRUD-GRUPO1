#encoding:utf-8
from django.forms import ModelForm
from school.models import Jornada

class JornadaForm(ModelForm):
    class Meta:
        model = Jornada
        # fields = ['name', 'description', 'is_active']