from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from .models import Takes, Course
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from bota.course import queue


def user(request):

    user_list = User.objects.all()
    context = {
        'user_list' : user_list,
    }
    template = loader.get_template('user.html')
    return HttpResponse(template.render(context, request))

def index(request):
    userTakes = Takes.objects.all()
    course = Course.objects.all()
    user = User.objects.all()
    currentUser = request.user
    context = {
        'currentUser' : currentUser,
        'takes' : userTakes,
        'course' : course,
        'user' : user,
    }
    template = loader.get_template('indexCourse.html')
    return HttpResponse(template.render(context, request))


def course(request, courseid):
    #= Course.objects.get(CourseID=courseid)
    context = {
        'ccourse': courseid,
    }
    template = loader.get_template('course.html')
    return HttpResponse(template.render(context, request))


def addMeToList(request, courseid):
    queue.addToQueue(courseid, request.user)
    context = {
        'posision': queue.getPosision(request.user, courseid),
        'ccourse': courseid,
    }
    template = loader.get_template('courseInQueue.html')
    return HttpResponse(template.render(context, request))

