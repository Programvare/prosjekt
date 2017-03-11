# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template import loader
from django.contrib.auth.views import login as auth_login
from django.contrib.auth import authenticate


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response


class botaUserCreationForm(UserCreationForm):

   class Meta(UserCreationForm.Meta):
       model = User
       fields = UserCreationForm.Meta.fields


def signup(request):
   # if this is a POST request we need to process the form data
   if request.method == 'POST':
       # create a form instance and populate it with data from the request:
       form = botaUserCreationForm(request.POST)
       # check whether it's valid:
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/course')

   # if a GET (or any other method) we'll create a blank form
   else:
       form = botaUserCreationForm()

   return render(request, 'registration/signup.html', {'form': form})

def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            if user.is_staff:
                return redirect('/settings')
            else:
                return redirect('/course')
        else:
            return render(request, 'registration/login.html', {})
    else:
        return render(request, 'registration/login.html', {})
