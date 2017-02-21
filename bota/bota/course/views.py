from django.http import HttpResponse
from django.template import loader
from .models import Takes, Course
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
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
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def course(request, courseid):

    ccourse = courseid
    #= Course.objects.get(CourseID=courseid)
    context = {
        'ccourse': ccourse,
    }
    template = loader.get_template('course.html')
    return HttpResponse(template.render(context, request))