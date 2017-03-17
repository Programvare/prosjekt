from django.conf.urls import url

from bota.app_settings import views

urlpatterns = [
    url(r'^$', views.settingsPage),
    url(r'courses$', views.courseEditPage),
    url(r'courses/((?P<courseid>[A-Z]{3}\d+)/del)', views.delCourse),
    url(r'((?P<courseid>[A-Z]{3}\d+)/delTakes)', views.delTakesCourse),
    url(r'courses/((?P<courseid>[A-Z]{3}\d+)/edit$)', views.editCourse),
    url(r'((?P<courseid>[A-Z]{3}\d+)/addTakes)', views.addTakesCourse),
    url(r'((?P<courseid>[A-Z]{3}\d+)/addTa$)', views.AddTAToCourse),
    url(r'((?P<courseid>[A-Z]{3}\d+)/addTa/(?P<username>\w{0,50})/)', views.AddTAToCourseUser),
    url(r'((?P<courseid>[A-Z]{3}\d+)/rmTa/(?P<username>\w{0,50})/)', views.rmTaFromCourse),
    url(r'((?P<courseid>[A-Z]{3}\d+)/editAs/(?P<id>\w{0,50})/)', views.editAs),
    url(r'((?P<courseid>[A-Z]{3}\d+)/addAs/)', views.addAs),
    url(r'((?P<courseid>[A-Z]{3}\d+)/rmAs/(?P<id>\w{0,50})/)', views.rmAs),
    url(r'editCourse', views.userEditCourses),
    url(r'courses/addCourse', views.addCourse),
    url(r'addTakes/$', views.addTakes, name='takes'),
]
