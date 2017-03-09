from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from bota.course.models import Takes, Course, TAin


@login_required(login_url='/login/')
def settingsPage(request):
    context = {'is_staff':request.user.is_staff}
    template = loader.get_template('settings.html')
    return HttpResponse(template.render(context, request))

@staff_member_required(login_url='/login/')
def courseEditPage(request):

    context = {
        'courses': Course.objects.all(),
    }
    template = loader.get_template('admin/courses.html')
    return HttpResponse(template.render(context, request))

@staff_member_required(login_url='/login/')
def delCourse(request, courseid):
    Course.objects.filter(CourseID = courseid).delete()
    return redirect('/settings/courses')

@login_required(login_url='/login/')
def delTakesCourse(request, courseid):
    Takes.objects.filter(CourseID__CourseID=courseid).\
        filter(UserID = request.user).delete()
    return redirect('/settings/editCourse')

@staff_member_required(login_url='/login/')
def addCourse(request):
    context = {}
    if request.method == "POST":
        CourseID = request.POST.get("CourseID")
        name = request.POST.get("Name")
        nickname = request.POST.get("Nickname")
        term = request.POST.get("Term")
        description = request.POST.get("Description")

        if len(Course.objects.filter(CourseID=CourseID))==0:
            c = Course(CourseID=CourseID, Name=name, Term=term, Nickname=nickname, Description=description)
            c.save();
            return redirect('settings/courses')
        context = {
            'CourseIDError': "Course already exists",
            'CourseID': CourseID,
            'name':name,
            'term':term,
            'nickname':nickname,
            'description': description,
         }

    return render(request, 'admin/newCourse.html',context)



@staff_member_required(login_url='/login/')
def editCourse(request, courseid):
    course = Course.objects.get(CourseID=courseid)
    context = {
        'Course': course,
    }
    if request.method == "POST":
        course.CourseID = courseid
        course.Name = request.POST.get("Name")
        course.Nickname = request.POST.get("Nickname")
        course.Term = request.POST.get("Term")
        course.Description = request.POST.get("Description")

        course.save()
        return redirect('settings/courses')

    template = loader.get_template('admin/editCourse.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def addTakes(request):
    if not Takes.objects.filter(UserID=request.user).exists():
        courses = Course.objects.all()
    else:
        courses = Course.objects.exclude(id__in=Takes.objects.filter(UserID=request.user).values("CourseID"))
    context = {
        'courses': courses
    }
    template = loader.get_template('user/addTakes.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def addTakesCourse(request, courseid):
    c = Takes(CourseID=Course.objects.get(CourseID=courseid), UserID=request.user)
    c.save()
    return redirect('/settings/editCourse')

@login_required(login_url='/login/')
def userEditCourses(request):
    context = {
        'TAin': Course.objects.filter(id__in=TAin.objects.filter(UserID=request.user).values("CourseID")),
        'courses': Course.objects.filter(id__in=Takes.objects.filter(UserID=request.user).values("CourseID")),
    }
    template = loader.get_template('user/courseSettings.html')
    return HttpResponse(template.render(context, request))