from django.conf.urls import url

from bota.admin import views

urlpatterns = [
    url(r'^$', views.adminPage),
    url(r'courses$', views.courseEditPage),
    url(r'courses/((?P<courseid>[A-Z]{3}\d+)/del)', views.delCourse),
    url(r'courses/((?P<courseid>[A-Z]{3}\d+)/edit)', views.editCourse),
    url(r'courses/addCourse', views.addCourse),
]
