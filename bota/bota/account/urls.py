from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

#URLS FOR LOGGING IN/SIGNUP
#Custom login uses auth_views.login
urlpatterns = [
    url(r'login/$', auth_views.login, name='login'),
    url(r'logout/$', auth_views.logout, name='logout'),
    url(r'signup/$', views.signup, name='signup'),
]