from django.http import HttpResponseRedirect
from django.contrib.auth.views import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


class BotaUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


def signup(request):
    if request.method == 'POST':
        form = BotaUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/course')
    else:
        form = BotaUserCreationForm()
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


def change_password(request):
    return render(request, 'registration/change_password.html')

def promote_user(request):
    return render(request, 'list_users.html')