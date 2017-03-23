from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from bota.course.models import Takes, Course, TAin, Assignment, TATime
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def settingsPage(request):
    context = {'is_staff': request.user.is_staff}
    return render(request, 'settings.html', context)

#Staff account


@staff_member_required(login_url='/login/')
def list_courses(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'admin/list_of_courses.html', context)


@staff_member_required(login_url='/login/')
def add_course(request):

    if request.method == "POST":
        course_id = request.POST.get("course_id")
        name = request.POST.get("name")
        nickname = request.POST.get("nickname")
        term = request.POST.get("term")
        description = request.POST.get("description")

        if len(Course.objects.filter(CourseID=course_id)) == 0:
            c = Course(CourseID=course_id, Name=name, Term=term, Nickname=nickname, Description=description)
            c.save()
            return redirect('settings/courses')

        context = {
            'CourseIDError': "Course already exists",
            'course_id': course_id,
            'name':name,
            'term':term,
            'nickname':nickname,
            'description': description,
         }
        return render(request, 'admin/new_course.html', context)
    return render(request, 'admin/new_course.html')


@staff_member_required(login_url='/login/')
def edit_course(request, course_id):
    course = Course.objects.get(CourseID=course_id)
    context = {
        'assignment': Assignment.objects.filter(course__CourseID=course_id),
        'course': course,
        'ta_in': TAin.objects.filter(CourseID__CourseID=course_id),
        'ta_times': TATime.objects.filter(course__CourseID=course_id),
    }
    if request.method == "POST":
        course.CourseID = course_id
        course.Name = request.POST.get("name")
        course.Nickname = request.POST.get("nickname")
        course.Term = request.POST.get("term")
        course.Description = request.POST.get("description")
        course.save()
        return redirect('/settings/courses/' + course_id + '/edit')
    return render(request, 'admin/edit_course.html', context)


@staff_member_required(login_url='/login/')
def rm_course(request, course_id):
    Course.objects.filter(CourseID=course_id).delete()
    return redirect('/settings/courses')


@staff_member_required(login_url='/login/')
def add_ta_to_course(request, course_id):
    if not TAin.objects.filter(CourseID__CourseID=course_id).exists():
        user = User.objects.all()
    else:
        user = User.objects.exclude(id__in=TAin.objects.filter(CourseID__CourseID=course_id).values("UserID"))
    context = {
         'course_id': course_id,
         'tas': user,
    }
    return render(request, 'admin/add_ta_to_course.html', context)


@staff_member_required(login_url='/login/')
def add_ta_to_course_user(request, course_id, username):
    course = Course.objects.get(CourseID=course_id)
    user = User.objects.get(username=username)
    ta = TAin(CourseID=course, UserID=user)
    ta.save()
    return redirect('/settings/courses/'+course_id+'/edit')


@staff_member_required(login_url='/login/')
def rm_ta_from_course(request, course_id, username):
    TAin.objects.get(CourseID__CourseID=course_id, UserID__username=username).delete()
    return redirect('/settings/courses/'+course_id+'/edit')


@staff_member_required(login_url='/login/')
def rm_as(request, course_id, as_id):
    Assignment.objects.get(id=as_id).delete()
    return redirect('/settings/courses/'+course_id+'/edit')


@staff_member_required(login_url='/login/')
def add_as(request, course_id):
    context = {'course_id': course_id}
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        delivery_deadline = request.POST.get("delivery_deadline")
        demo_deadline = request.POST.get("demo_deadline")
        a = Assignment(course=Course.objects.get(CourseID=course_id), name=name, description=description,
                       delivery_deadline=delivery_deadline, demo_deadline=demo_deadline)
        a.save()
        return redirect('/settings/courses/'+course_id+'/edit')
    return render(request, 'admin/new_as.html', context)


@staff_member_required(login_url='/login/')
def edit_as(request, as_id, course_id):
    a = Assignment.objects.get(id=as_id)
    context = {'assignment': a,
               'delivery_deadline': str(a.delivery_deadline.date()) + "T" + str(a.delivery_deadline.time()),
               'demo_deadline': str(a.demo_deadline.date()) + "T" + str(a.demo_deadline.time()),
               'course_id': course_id,
               }
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        delivery_deadline = request.POST.get("delivery_deadline")
        demo_deadline = request.POST.get("demo_deadline")
        a.course = Course.objects.get(CourseID=course_id)
        a.name = name
        a.description = description
        a.delivery_deadline = delivery_deadline
        a.demo_deadline = demo_deadline
        a.save()
        return redirect('/settings/courses/'+course_id+'/edit')
    return render(request, 'admin/edit_as.html', context)


@staff_member_required(login_url='/login/')
def add_ta_time(request, course_id):
    context = {'course_id': course_id}
    if request.method == "POST":
        course = Course.objects.get(CourseID=course_id)
        date = request.POST.get("date")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        teaching_assistant = request.POST.get("teaching_assistant")
        room = request.POST.get("room")
        tat = TATime(course=course,
                     date=date,
                     start_time=start_time,
                     end_time=end_time,
                     teaching_assistant=teaching_assistant,
                     room=room)
        tat.save()
        return redirect('/settings/courses/' + course_id + '/edit')
    return render(request, 'admin/new_ta_time.html', context)


@staff_member_required(login_url='/login/')
def edit_ta_time(request, ta_id, course_id):
    tat = TATime.objects.get(id=ta_id)
    context = {'tat': tat,
               'date': str(tat.date),
               'start_time': str(tat.start_time),
               'end_time': str(tat.end_time),
               'teaching_assistant': tat.teaching_assistant,
               'room': tat.room,
               'course_id': course_id,
               'ta_id': tat.id}
    if request.method == "POST":
        tat.course = Course.objects.get(CourseID=course_id)
        tat.date = request.POST.get("date")
        tat.start_time = request.POST.get("start_time")
        tat.end_time = request.POST.get("end_time")
        tat.teaching_assistant = request.POST.get("teaching_assistant")
        tat.room = request.POST.get("room")
        tat.save()
        return redirect('/settings/courses/' + course_id + '/edit')
    return render(request, 'admin/edit_ta_time.html', context)


@staff_member_required(login_url='/login/')
def rm_ta_time(request, course_id, ta_id):
    TATime.objects.get(id=ta_id).delete()
    return redirect('/settings/courses/'+course_id+'/edit')


#User


@login_required(login_url='/login/')
def add_takes(request):
    if not Takes.objects.filter(UserID=request.user).exists():
        courses = Course.objects.all()
    else:
        courses = Course.objects.exclude(id__in=Takes.objects.filter(UserID=request.user).values("CourseID"))
    context = {'courses': courses}
    return render(request, 'user/add_takes_course.html', context)


@login_required(login_url='/login/')
def rm_takes_course(request, course_id):
    Takes.objects.filter(CourseID__CourseID=course_id).filter(UserID=request.user).delete()
    return redirect('/settings/edit_course')


@login_required(login_url='/login/')
def add_takes_course(request, course_id):
    c = Takes(CourseID=Course.objects.get(CourseID=course_id), UserID=request.user)
    c.save()
    return redirect('/settings/edit_course')


@login_required(login_url='/login/')
def user_list_courses(request):
    context = {
        'TAin': Course.objects.filter(id__in=TAin.objects.filter(UserID=request.user).values("CourseID")),
        'courses': Course.objects.filter(id__in=Takes.objects.filter(UserID=request.user).values("CourseID")),
    }
    return render(request, 'user/list_of_courses.html', context)

