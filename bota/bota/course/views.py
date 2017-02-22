from django.http import HttpResponse
from django.template import loader
from .models import Takes, Course
from bota.course import queue
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def courseMainPage(request):
    context = {
        'currentUser' : request.user,
        'takes' : Takes.objects.all(),
        'course' : Course.objects.all(),
    }
    template = loader.get_template('mainCoursePage.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def course(request, courseid):
    context = {
        'ccourse': courseid,
    }
    template = loader.get_template('course.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def addMeToList(request, courseid):
    queue.addToQueue(request.user, courseid)
    context = {
        'posision': queue.getPosision(request.user, courseid),
        'ccourse': courseid,
    }
    template = loader.get_template('courseInQueue.html')
    return HttpResponse(template.render(context, request))

