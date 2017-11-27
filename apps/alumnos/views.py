from django.shortcuts import render,redirect
from django.http import HttpResponse
from apps.alumnos.forms import AlumnosForm
from apps.alumnos.models import Alumnos
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

def index(request):
    return render(request,'base/base.html')

"""def alumnos_view(request):
    if request.method=='POST':
        form=AlumnosForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form=AlumnosForm()
    return  render(request,'base/alumnos/alumnos_form.html',{'form':form})
"""
"""def alumnos_list(request):
    qalumnos=Alumnos.objects.all()
    contexto={'alumnos':qalumnos }
    return render(request, 'base/alumnos/alumnos_list.html',contexto)"""
"""
def alumnos_edit(request,id_alumnos):
    qalumnos=Alumnos.objects.get(id=id_alumnos)
    if request.method=='GET':
        form = AlumnosForm(instance=qalumnos)
    else:
        form=AlumnosForm(request.POST,instance=qalumnos)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'base/alumnos/alumnos_form.html',{'form':form})
"""
class AlumnosList(ListView):
    model = Alumnos
    template_name = 'base/alumnos/alumnos_list.html'
    paginate_by = 10

class AlumnosCrear(CreateView):
    model = Alumnos
    form_class = AlumnosForm
    template_name = 'base/alumnos/alumnos_form.html'
    success_url = reverse_lazy('alumnos:alumnos_listar')

class AlumnoEdit(UpdateView):
    model = Alumnos
    form_class = AlumnosForm
    template_name = 'base/alumnos/alumnos_form.html'
    success_url = reverse_lazy('alumnos:alumnos_listar')

class AlumnoBorrar(DeleteView):
    model = Alumnos
    template_name = 'base/alumnos/Alumno_borrar.html'
    success_url = reverse_lazy('alumnos:alumnos_listar')
