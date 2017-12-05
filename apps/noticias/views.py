from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from apps.noticias.models import noticias
from .forms import noticiaform
from django.template import RequestContext


class noticiasListar(ListView):
    model = noticias
    template_name = 'base/noticias/index.html'
    paginate_by = 10

class noticiasCrear(CreateView):
    model = noticias
    form_class = noticiaform
    template_name = 'base/noticias/crear.html'
    success_url = reverse_lazy('noticias:noticiaListar')

class noticiasDetalle(DetailView):
    model = noticias
    template_name = 'base/noticias/detalle.html'
