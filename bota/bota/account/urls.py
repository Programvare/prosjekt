from django.conf.urls import url
from django.contrib.auth import views as auth_views
from bota import views

urlpatterns = [
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]