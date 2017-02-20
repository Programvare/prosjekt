from django.http import HttpResponse
from django.template import loader
from .models import User, Takes, Course

def index(request):

    user_list = User.objects.all()
    context = {
        'user_list' : user_list,
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def user(request):
    userTakes = Takes.objects.all()
    course = Course.objects.all()
    user = User.objects.all()
    context = {
        'takes' : userTakes,
        'course' : course,
        'user' : user,
    }
    template = loader.get_template('user.html')
    return HttpResponse(template.render(context, request))
