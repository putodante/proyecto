from django.conf.urls import url,include
from  django.contrib.auth.decorators import login_required
from apps.alumnos.views import index,AlumnosCrear,AlumnosList,AlumnoEdit,AlumnoBorrar

urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^nuevo$',login_required(AlumnosCrear.as_view()),name='alumnos_crear'),
    url(r'^listar$', login_required(AlumnosList.as_view()), name='alumnos_listar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(AlumnoEdit.as_view()), name='alumnos_editar'),
    url(r'^borrar/(?P<pk>\d+)/$', login_required(AlumnoBorrar.as_view()),name='alumnos_borrar'),

]