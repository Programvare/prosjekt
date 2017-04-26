# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render

"""
Loads landing page, if you are loggedin you will be redirected to the course page
or settings page if you are an Admin
"""
def main_page(request):
    if request.user.is_authenticated():
        if request.user.is_staff:
            return redirect('/settings')
        return redirect('/course')
    return render(request, 'index.html', {})


