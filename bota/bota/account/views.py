# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.views import login

#Placeholder function.
#Use decorators in front of views that require logins
#https://docs.djangoproject.com/en/1.10/topics/auth/default/#the-login-required-decorator

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

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


# This uses the contrib.auth.views.login
# See: https://docs.djangoproject.com/en/1.10/topics/auth/default/#all-authentication-views
# To see what it does. Notably automagically renders registration/login.html
# The redirection after post is specified in "next" in URLS
def custom_login(request):
   login(request)

#NOTE: logout method is autoredirection to some page, see URLS