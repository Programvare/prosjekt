from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Takes, Course, TAin, TATime
from bota.course import queue
from django.contrib.auth.decorators import login_required
import datetime


@login_required(login_url='/login/')
def courseMainPage(request):
    context = {
        'currentUser': request.user,
        'takes': Takes.objects.all(),
        'TAin': TAin.objects.all(),
        'course': Course.objects.all(),
    }
    template = loader.get_template('mainCoursePage.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def course(request, courseid):
    # Get list of all ta times for course
    try:
        all_tatimes = TATime.objects.filter(course__CourseID=courseid).order_by('date')
    except TATime.DoesNotExist:
        all_tatimes = []
    # Display only current weeks ta times
    tatimes = []
    for time in all_tatimes:
        if time.date.isocalendar()[1] == datetime.date.today().isocalendar()[1]:
            tatimes.append(time)
    # Check if there currently is a ta time, i.e. can students enter the queue?
    now = datetime.datetime.today()
    can_enter = False
    for time in tatimes:
        if time.date == now.date():
            if now.time() >= time.start_time and now.time() <= time.end_time:
                can_enter = True

    context = {
        'posision': queue.getPosision(request.user, courseid),
        'ccourse': courseid,
        'tatimes': tatimes,
        'can_enter': can_enter,
    }
    if queue.userInQueue(request.user, courseid):
        template = loader.get_template('courseInQueue.html')
        return HttpResponse(template.render(context, request))
    template = loader.get_template('course.html')
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
    context = {
        'posision': queue.getPosision(request.user, courseid),
        'ccourse': courseid,
    }
    template = loader.get_template('courseInQueue.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def removeFromCourse(request, courseid):
    queue.removeFromQueue(courseid)
    context = {
        'ccourse': courseid,
        'next' : queue.getNext(courseid),
    }
    template = loader.get_template('courseTA.html')
    return HttpResponse(template.render(context, request))


@login_required(login_url='/login/')
def taTimes(request, courseid):
    try:
        all_tatimes = TATime.objects.filter(course__CourseID=courseid).order_by('date')
    except TATime.DoesNotExist:
        all_tatimes = []

    context = {
        'ta_time_list': all_tatimes,
        'ccourse': courseid
    }

    template = loader.get_template('ta_time.html')
    return HttpResponse(template.render(context, request))
