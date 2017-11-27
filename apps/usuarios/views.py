from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from apps.usuarios.forms import RegistroUsuario

class RegistroUsuario(CreateView):
    model = User
    template_name = "base/usuario/registrar.html"
    form_class = RegistroUsuario
    success_url = reverse_lazy('alumnos:alumnos_listar')


# Create your views here.
