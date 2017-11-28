from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import login,logout_then_login, password_reset,password_reset_done,password_reset_confirm,password_reset_complete

urlpatterns = [
    url(r'^$',login,{'template_name':'index.html'},name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/',login,{'template_name':'index.html'},name='login'),
    url(r'^alumnos/', include('apps.alumnos.urls',namespace='alumnos')),
    url(r'^profesores/', include('apps.profesores.urls',namespace='profesores')),
    url(r'^usuario/',include('apps.usuarios.urls',namespace='usuario')),
    url(r'^logout/',logout_then_login,name='logout'),

    url(r'^reset/password_reset', password_reset,{'template_name':'base/recuperar/pass_reset_form.html','email_template_name':'base/recuperar/pass_reset_email.html'},name='password_reset'),
    url(r'^reset/password_reset_done',password_reset_done,{'template_name':'base/recuperar/pass_reset_done.html'},name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm,{'template_name': 'base/recuperar/pass_reset_confirm.html'},name='password_reset_confirm'),
    url(r'^reset/done', password_reset_complete,{'template_name':'base/recuperar/pass_reset_complete.html'},name='password_reset_complete')
]
