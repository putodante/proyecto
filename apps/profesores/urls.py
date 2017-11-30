from django.conf.urls import url,include
from apps.profesores.views import ProfesoresList,ProfesoresCrear,ProfesoresBorrar,ProfesoresEditar
from  django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^listar$',login_required(ProfesoresList.as_view()),name='profesores_list'),
    url(r'^nuevo$', login_required(ProfesoresCrear.as_view()), name='profesores_crear'),
    url(r'^borrar/(?P<pk>\d+)/$',login_required(ProfesoresBorrar.as_view()), name='profesores_borrar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(ProfesoresEditar.as_view()), name='profesores_editar')
]