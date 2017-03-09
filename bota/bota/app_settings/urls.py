from django.conf.urls import url

from bota.app_settings import views

urlpatterns = [
    url(r'^$', views.settingsPage),
    url(r'courses$', views.courseEditPage),
    url(r'courses/((?P<courseid>[A-Z]{3}\d+)/del)', views.delCourse),
    url(r'((?P<courseid>[A-Z]{3}\d+)/delTakes)', views.delTakesCourse),
    url(r'courses/((?P<courseid>[A-Z]{3}\d+)/edit)', views.editCourse),
    url(r'((?P<courseid>[A-Z]{3}\d+)/addTakes)', views.addTakesCourse),
    url(r'editCourse', views.userEditCourses),
    url(r'courses/addCourse', views.addCourse),
    url(r'addTakes/$', views.addTakes, name='takes'),
]