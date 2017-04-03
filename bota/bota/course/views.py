from django.shortcuts import render
from .models import Takes, Course, TAin, TATime, Assignment
from bota.course import queue
from django.contrib.auth.decorators import login_required
import datetime


@login_required(login_url='/login/')
def course_main_page(request):
    context = {
        'ta_in': Course.objects.filter(id__in=TAin.objects.filter(user_id=request.user).values("course_id")),
        'courses': Course.objects.filter(id__in=Takes.objects.filter(user_id=request.user).values("course_id")),
        'assignments': get_all_student_assignments(request)
    }
    return render(request, 'main_course_page.html', context)


def course(request, course_id):

    ta_times = get_week_times(course_id)
    all_ta_times = get_all_times_after_week(course_id)
    can_enter = check_can_enter(course_id)

    assignments = get_all_course_assignments(course_id)

    course_model = Course.objects.get(course_id=course_id)

    context = {
        'course_model': course_model,
        'course_id': course_id,
        'position': queue.get_position(request.user, course_id),
        'ta_times': ta_times,
        'can_enter': can_enter,
        'assignments': assignments,
        'all_ta_times': all_ta_times,
        'queue_length': queue.get_length(course_id),
    }

    if queue.user_in_queue(request.user, course_id):
        return render(request, 'course_in_queue.html', context)
    return render(request, 'course.html', context)


def course_position(request):
    #The problem with having a separate view for a _div_
    #is that we can't have a fancy context-based url in urls.py
    #request.META gives the current url path. index [-2] should return the current courseid
    course_id = request.META['HTTP_REFERER'].split('/')[-2]
    position = queue.get_position(request.user, course_id)

    context = {
        'course_model': Course.objects.get(course_id=course_id),
        'position': position,
        'course_id': course_id,
    }
    return render(request, 'course_position_div.html', context)


@login_required(login_url='/login/')
def course_ta_next(request):
    #The problem with having a separate view for a _div_
    #is that we can't have a fancy context-based url in urls.py
    #request.META gives the current url path. index [-2] should return the current courseid
    course_id = request.META['HTTP_REFERER'].split('/')[-2]
    next_queue = queue.get_next(course_id)
    queue_length = queue.get_length(course_id)

    context = {
        'next': next_queue,
        'queue_length': queue_length,
        'course_model': Course.objects.get(course_id=course_id),
        'course_id': course_id,
    }
    return render(request, 'course_ta_next_div.html', context)


@login_required(login_url='/login/')
def course_ta(request, course_id):
    context = {
        'course_id': course_id,
        'next': queue.get_next(course_id),
        'queue_length': queue.get_length(course_id),
        'course_model': Course.objects.get(course_id=course_id),
    }
    return render(request, 'course_ta.html', context)


@login_required(login_url='/login/')
def add_me_to_list(request, course_id):
    if check_can_enter(course_id):
        queue.add_to_queue(request.user, course_id)
    return course(request, course_id)


@login_required(login_url='/login/')
def rm_from_course(request, course_id):
    queue.rm_from_queue(course_id)
    context = {
        'course_id': course_id,
        'next': queue.get_next(course_id),
        'queue_length': queue.get_length(course_id),
        'course_model': Course.objects.get(course_id=course_id),
    }
    return render(request, 'course_ta.html', context)


"""
Removed and placed in div
@login_required(login_url='/login/')
def taTimes(request, courseid):
    all_tatimes = get_all_times(courseid)

    context = {
        'ta_time_list': all_tatimes,
        'ccourse': courseid
    }

    template = loader.get_template('ta_time.html')
    return HttpResponse(template.render(context, request))
"""

# Help functions #


def get_all_times(course_id):
    # Get list of all ta times for course
    try:
        all_ta_times = TATime.objects.filter(course__course_id=course_id).order_by('date')
    except TATime.DoesNotExist:
        all_ta_times = []
    # Remove "old" times from list
    ta_times = []
    for time in all_ta_times:
        if time.date >= datetime.date.today():
            ta_times.append(time)
    return ta_times


def get_all_times_after_week(course_id):
    try:
        all_ta_times = TATime.objects.filter(course__course_id=course_id).order_by('date')
    except TATime.DoesNotExist:
        all_ta_times = []
    # Remove "old" times from list
    ta_times = []
    for time in all_ta_times:
        if time.date.isocalendar()[1] == datetime.date.today().isocalendar()[1] + 1:
            ta_times.append(time)
    return ta_times


def get_week_times(course_id):
    # Display only current weeks ta times
    ta_times = []
    all_ta_times = get_all_times(course_id)
    for time in all_ta_times:
        if time.date.isocalendar()[1] == datetime.date.today().isocalendar()[1]:
            ta_times.append(time)
    return ta_times


def check_can_enter(course_id):
    ta_times = get_all_times(course_id)
    # Check if there currently is a ta time, i.e. can students enter the queue?
    now = datetime.datetime.today()
    can_enter = False
    for time in ta_times:
        if time.date == now.date():
            if now.time() >= time.start_time and now.time() <= time.end_time:
                can_enter = True
    return can_enter


def get_all_course_assignments(course_id):
    # Get list of all assignments for course
    try:
        all_assignments = Assignment.objects.filter(course__course_id=course_id).order_by('delivery_deadline')
    except Assignment.DoesNotExist:
        all_assignments = []
    # Remove "old" assignments from list
    assignments = []
    for assignment in all_assignments:
        if assignment.demo_deadline >= datetime.datetime.today():
            assignments.append(assignment)
    return assignments


def get_all_student_assignments(request):
    # Get list of all assignments for student
    assignments = []
    try:
        courses = Course.objects.filter(id__in=Takes.objects.filter(user_id=request.user).values("course_id"))
        for course_id in courses:
            course_assignments = get_all_course_assignments(course_id)
            for assignment in course_assignments:
                assignments.append(assignment)
    except Assignment.DoesNotExist:
        assignments = []
    return assignments


