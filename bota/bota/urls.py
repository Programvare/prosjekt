"""bota URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from bota import views

urlpatterns = [
    url(r'^$', views.mainPage),
    url(r'^', include('bota.account.urls')),
    url(r'^admin/', views.adminPage),
    url(r'^course', include('bota.course.urls')),

]

#url(r'^login_site$', views.showlogin),
#url(r'^login$', views.login),
#url(r'^$', views.showMainPage),