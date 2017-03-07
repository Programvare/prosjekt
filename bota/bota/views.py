# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse

def mainPage(request):
    if request.user.is_authenticated():
        return redirect('/course')
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))


