# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse


def main_page(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return redirect('/settings')
        return redirect('/course')
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))


