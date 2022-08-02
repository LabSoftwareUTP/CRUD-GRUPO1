# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from school.models import Jornada
from school.models import ProgramasAcademico
from django.template import RequestContext

def getAllJornadas():
	try:
		_jornadas = Jornada.objects.all()
	except Jornada.DoesNotExist:
		_jornadas = None
	return _jornadas


def getJornadaById(id_jornada):
	try:
		art = Jornada.objects.get(pk=id_jornada)
	except Jornada.DoesNotExist:
		art = None
	return art


def listarJornadas(request):
	ctx ={
		"jornadas" : getAllJornadas()
	}
	return render(request, "index.html", ctx)


def newJornada(request):
	from school.forms import JornadaForm
	if request.method == "POST":
		form = JornadaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/jornadas#agregada")
	else:
		form = JornadaForm()
	ctx ={
		"formulario": form
	}
	return render(request, "form.html", ctx)


def editJornada(request, id_jornada):
	art = getJornadaById(id_jornada)
	from school.forms import JornadaForm
	if request.method == "POST":
		form = JornadaForm(request.POST, instance=art)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/jornadas#editada")
	else:
		if art:
			form = JornadaForm(instance=art)
		else:
			return HttpResponseRedirect("/jornadas#no-existe-esa-jornada")
	ctx ={
		"formulario": form
	}
	return render(request, "form.html", ctx, context_instance=RequestContext(request))

from django.db.models.deletion import Collector
from django.db import router


def get_related(queryset):
    using = router.db_for_read(queryset.model)
    coll = Collector(using=using)
    coll.collect(queryset)
    return coll.data


def deleteJornada(request, id_jornada):
	_jornada = getJornadaById(id_jornada)
	if _jornada:
		if request.method == "POST":
			_jornada.delete()
		else:
			related_objs = _jornada.related_programas.all()
			ctx = {
				"obj": _jornada,
				"related_objs": related_objs
			}
			return render(request, "delete_confirm.html", ctx, context_instance=RequestContext(request))
		return HttpResponseRedirect("/jornadas#eliminado")
	return HttpResponseRedirect("/#no-hay-jornada-a-eliminar")

def getAllPAcademico():
	try:
		_jornadas = ProgramasAcademico.objects.all()
	except ProgramasAcademico.DoesNotExist:
		_jornadas = None
	return _jornadas


def getPAcademicoById(id_pAcademico):
	try:
		art = ProgramasAcademico.objects.get(pk=id_pAcademico)
	except ProgramasAcademico.DoesNotExist:
		art = None
	return art


def listarPAcademico(request):
	ctx ={
		"programas" : getAllPAcademico()
	}
	return render(request, "index_programs.html", ctx)


def newPAcademico(request):
	from school.forms import PAcademicoForm
	if request.method == "POST":
		form = PAcademicoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/programas#agregada")
	else:
		form = PAcademicoForm()
	ctx ={
		"formulario": form
	}
	return render(request, "form_programs.html", ctx, context_instance=RequestContext(request))


def editPAcademico(request, id_pAcademico):
	art = getPAcademicoById(id_pAcademico)
	from school.forms import PAcademicoForm
	if request.method == "POST":
		form = PAcademicoForm(request.POST, instance=art)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/programas#editada")
	else:
		if art:
			form = PAcademicoForm(instance=art)
		else:
			return HttpResponseRedirect("/programas#no-existe-esa-jornada")
	ctx ={
		"formulario": form
	}
	return render(request, "form_programs.html", ctx, context_instance=RequestContext(request))


def deletePAcademico(request, id_pAcademico):
	art = getPAcademicoById(id_pAcademico)
	if art:
		art.delete()
		return HttpResponseRedirect("/programas#eliminado")
	return HttpResponseRedirect("/#no-hay-jornada-a-eliminar")