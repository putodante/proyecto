from django.conf.urls import url,include
from apps.profesores.views import index_profesores,ProfesoresList

urlpatterns = [
    url(r'^index$',index_profesores),
    url(r'^listar$',ProfesoresList.as_view(),name='profesres_list')
]