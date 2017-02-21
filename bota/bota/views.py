# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse


def showlogin(request):
    template = loader.get_template('registration/login.html')
    return HttpResponse(template.render(request))
