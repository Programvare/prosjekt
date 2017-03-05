from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from bota.course.models import Course

from django.contrib.auth.decorators import login_required


def adminPage(request):
    template = loader.get_template('admin/admin.html')
    return HttpResponse(template.render(request))

def courseEditPage(request):

    context = {
        'courses': Course.objects.all(),
    }

    template = loader.get_template('admin/courses.html')
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def delCourse(request, courseid):
    Course.objects.filter(CourseID = courseid).delete()
    return redirect('/admin/courses')

@login_required(login_url='/login/')
def addCourse(request):
    template = loader.get_template('admin/newCourse.html')
    return HttpResponse(template.render(request))

@login_required(login_url='/login/')
def editCourse(request):
    template = loader.get_template('admin/editCourse.html')
    return HttpResponse(template.render(request))
