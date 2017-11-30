from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from apps.profesores.models import profesores
from apps.profesores.forms import ProfesorForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class ProfesoresList(ListView):
    model = profesores
    template_name = 'base/profesores/profesores_list.html'
    paginate_by = 10

class ProfesoresCrear(CreateView):
    model = profesores
    form_class = ProfesorForm
    template_name = 'base/profesores/profesores_create.html'
    success_url =  reverse_lazy('profesores:profesores_list')

class ProfesoresBorrar(DeleteView):
    model = profesores
    template_name = 'base/profesores/profesores_borrar.html'
    success_url = reverse_lazy('profesores:profesores_list')

class ProfesoresEditar(UpdateView):
    model = profesores
    form_class = ProfesorForm
    template_name = 'base/profesores/profesores_create.html'
    success_url =  reverse_lazy('profesores:profesores_list')
