from django.conf.urls import url
from bota.app_settings import views

urlpatterns = [
    url(r'^$', views.settingsPage),

    url(r'courses$', views.list_courses),

    url(r'courses/add_course', views.add_course),
    url(r'courses/((?P<course_id>[A-Z]{3}\d+)/edit$)', views.edit_course),
    url(r'courses/((?P<course_id>[A-Z]{3}\d+)/rm_course)', views.rm_course),
    url(r'((?P<course_id>[A-Z]{3}\d+)/add_ta$)', views.add_ta_to_course),
    url(r'((?P<course_id>[A-Z]{3}\d+)/add_ta/(?P<username>\w{0,50})/)', views.add_ta_to_course_user),
    url(r'((?P<course_id>[A-Z]{3}\d+)/rm_ta/(?P<username>\w{0,50})/)', views.rm_ta_from_course),
    url(r'((?P<course_id>[A-Z]{3}\d+)/edit_as/(?P<as_id>\w{0,50})/)', views.edit_as),
    url(r'((?P<course_id>[A-Z]{3}\d+)/add_as/)', views.add_as),
    url(r'((?P<course_id>[A-Z]{3}\d+)/rm_as/(?P<as_id>\w{0,50})/)', views.rm_as),
    url(r'((?P<course_id>[A-Z]{3}\d+)/add_ta_time/)', views.add_ta_time),
    url(r'((?P<course_id>[A-Z]{3}\d+)/rm_ta_time/(?P<ta_id>\w{0,50})/)', views.rm_ta_time),
    url(r'((?P<course_id>[A-Z]{3}\d+)/edit_ta_time/(?P<ta_id>\w{0,50})/)', views.edit_ta_time),

    url(r'add_takes/$', views.add_takes),
    url(r'edit_course$', views.user_list_courses),
    url(r'((?P<course_id>[A-Z]{3}\d+)/add_takes)', views.add_takes_course),
    url(r'((?P<course_id>[A-Z]{3}\d+)/rm_takes)', views.rm_takes_course),


]
