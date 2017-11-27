from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView
from apps.profesores.models import profesores
from apps.profesores.forms import ProfesorForm
# Create your views here.
def index_profesores(request):
    return HttpResponse("soy la pagina de los profesores")

class ProfesoresList(ListView):
    model = profesores
    template_name = 'base/profesores/profesores_list.html'

class ProfesoresCrear(CreateView):
    model = profesores
    template_name = 'base/profesores'
    form_class = ProfesorForm
