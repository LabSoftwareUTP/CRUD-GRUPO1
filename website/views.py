# Create your views here.
from django.http import HttpResponseRedirect


def home(request):
	return HttpResponseRedirect("/programas")
