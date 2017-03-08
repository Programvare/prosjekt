from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Takes, Course, TAin
from bota.course import queue
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def courseMainPage(request):
    context = {
        'currentUser' : request.user,
        'takes' : Takes.objects.all(),
        'TAin' : TAin.objects.all(),
        'course' : Course.objects.all(),
    }
    template = loader.get_template('mainCoursePage.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def course(request, courseid):

    context = {
        'posision': queue.getPosision(request.user, courseid),
        'ccourse': courseid,
    }
    if queue.userInQueue(request.user, courseid):
        template = loader.get_template('courseInQueue.html')
        return HttpResponse(template.render(context, request))

    template = loader.get_template('course.html')
    return HttpResponse(template.render(context, request))

def course_position(request):
    #The problem with having a separate view for a _div_
    #is that we can't have a fancy context-based url in urls.py
    #request.META gives the current url path. index [-2] should return the current courseid
    courseid = request.META['HTTP_REFERER'].split('/')[-2]
    position = queue.getPosision(request.user, courseid)

    context = {
        'posision': position,
        'ccourse': courseid,
    }

    template = loader.get_template('course_position_div.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def courseTA(request, courseid):
    context = {
        'ccourse': courseid,
        'next' : queue.getNext(courseid),
    }
    template = loader.get_template('courseTA.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def addMeToList(request, courseid):
    queue.addToQueue(request.user, courseid)
    return course(request, courseid)


@login_required(login_url='/login/')
def removeFromCourse(request, courseid):
    queue.removeFromQueue(courseid)
    context = {
        'ccourse': courseid,
        'next' : queue.getNext(courseid),
    }
    template = loader.get_template('courseTA.html')
    return HttpResponse(template.render(context, request))



"""def ta_time(request, courseid):
    try:
        ta_time_list = TATime.objects.filter(course=courseid)
        print(ta_time_list)
    except TATime.DoesNotExist:
        ta_time_list = []
    context = {'ta_time_list': ta_time_list}
    return render(request, 'course/ta_time.html', context)
"""

"""context = {
    'posision': queue.getPosision(request.user, courseid),
    'ccourse': courseid,
    'hello': courseid,
}
template = loader.get_template('courseInQueue.html')
return HttpResponse(template.render(context, request))
"""