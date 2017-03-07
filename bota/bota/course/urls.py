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
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.courseMainPage, name='index'),
    url(r'addTakes$', views.addTakes, name='takes'),
    url(r'((?P<courseid>[A-Z]{3}\d+)/TA$)', views.courseTA),
    url(r'((?P<scourseid>[A-Z]{3}\d+)/$)', views.course),
    url(r'((?P<courseid>[A-Z]{3}\d+)/addCourse)', views.addTakesCourse),
    url(r'((?P<courseid>[A-Z]{3}\d+)/inQueue)', views.addMeToList),
    url(r'((?P<courseid>[A-Z]{3}\d+)/rmQueue)', views.removeFromCourse),
    url(r'((?P<courseid>[A-Z]{3}\d+)/taTimes)', views.taTimes),

]
