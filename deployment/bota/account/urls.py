from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name="login"),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^promote_user/$', views.promote_user_list, name='signup'),
    url(r'^promote_user/((?P<username>([A-Z a-z])\w+))$', views.promote_user, name='signup'),
]