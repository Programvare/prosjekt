# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render


def main_page(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return redirect('/settings')
        return redirect('/course')
    return render(request, 'index.html', {})


