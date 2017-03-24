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
from bota.course import views

app_name = 'course'

urlpatterns = [
    url(r'^$', views.course_main_page, name='index'),
    url(r'((?P<course_id>[A-Z]{3}\d+)/ta$)', views.course_ta),
    url(r'((?P<course_id>[A-Z]{3}\d+)/$)', views.course, name='course'),
    url(r'((?P<course_id>[A-Z]{3}\d+)/in_queue)', views.add_me_to_list),
    url(r'((?P<course_id>[A-Z]{3}\d+)/rm_queue)', views.rm_from_course),
    url(r'^course_position/$', views.course_position, name='course_position'),
    url(r'^course_next/$', views.course_ta_next, name='course_next'),


]

#url(r'((?P<courseid>[A-Z]{3}\d+)/taTimes)', views.taTimes),