from django.conf.urls import url,include
from  django.contrib.auth.decorators import login_required

from apps.noticias import views
from .views import noticiasCrear,noticiasListar,noticiasDetalle

urlpatterns=[
    url(r'^crear$',login_required(noticiasCrear.as_view()),name='noticiaCrear'),
    url(r'^listar$',login_required(noticiasListar.as_view()),name='noticiaListar'),
    url(r'^ver/(?P<pk>\d+)/$', login_required(noticiasDetalle.as_view()), name='Noticiasdetale'),
]