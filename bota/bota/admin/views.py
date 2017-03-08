from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from bota.course.models import Course
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(login_url='/login/')
def adminPage(request):
    template = loader.get_template('admin/admin.html')
    return HttpResponse(template.render(request))

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
    return redirect('/admin/courses')

@staff_member_required(login_url='/login/')
def addCourse(request):
    if request.method == "POST":
        courseID = request.POST.get("CourseID")
        name = request.POST.get("Name")
        term = request.POST.get("Term")
        description = request.POST.get("Description")
        c = Course(CourseID=courseID, Name=name, Term=term, Description=description)
        c.save();
        return redirect('admin/courses')

    return render(request, 'admin/newCourse.html', {})



@staff_member_required(login_url='/login/')
def editCourse(request, courseid):
    context = {
        'Course': Course.objects.get(CourseID=courseid),
    }
    template = loader.get_template('admin/newCourse.html')
    return HttpResponse(template.render(context, request))
