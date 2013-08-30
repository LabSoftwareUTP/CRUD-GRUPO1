# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from school.models import Jornada
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
	return render_to_response("index.html", ctx)


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
	return render_to_response("form.html", ctx, context_instance=RequestContext(request))


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
	return render_to_response("form.html", ctx, context_instance=RequestContext(request))


def deleteJornada(request, id_jornada):
	art = getJornadaById(id_jornada)
	if art:
		art.delete()
		return HttpResponseRedirect("/jornadas#eliminado")
	return HttpResponseRedirect("/#no-hay-jornada-a-eliminar")
