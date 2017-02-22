# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


from bota.course import views

def showlogin(request):
    template = loader.get_template('registration/login.html')
    return HttpResponse(template.render(request))

def showMainPage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))


def login(request):
    print(request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(views.index())
        else:
            # Return a 'disabled account' error message
            return HttpResponse('error')
    else:
        return HttpResponse('error')