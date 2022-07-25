#encoding:utf-8
from tkinter import CASCADE
from django.db import models


class Jornada(models.Model):
    name = models.CharField(max_length=150, verbose_name="name")
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def get_foreign_fields(self):
      return [getattr(self, f.name) for f in self._meta.fields if type(f) == models.fields.related.ForeignKey]

    def __unicode__(self):
        return "%s" % (self.name)


class ProgramasAcademico(models.Model):
	
	nombre = models.CharField(max_length=100, null=False)
	activo = models.BooleanField(default=True, null=False)
	fecha_creacion = models.DateField(auto_now_add=True, null=False)
	id_jornada = models.ForeignKey(Jornada, null=False, related_name='related_programas', on_delete=models.CASCADE)
	
	def __unicode__(self):
			return self.nombre