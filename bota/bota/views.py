# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from bota.course import views

def mainPage(request):
    if request.user.is_authenticated():
        return redirect('/course')
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))


def adminPage(request):
    template = loader.get_template('admin/admin.html')
    return HttpResponse(template.render(request))