from django.http import HttpResponseRedirect
from django.contrib.auth.views import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


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
    error = ""
    if request.method == 'POST':
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
                error = "Your username and password didn't match. Please try again."
        else:
            error = "Your username and password didn't match. Please try again."
    return render(request, 'registration/login.html', {'error': error})

@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('/settings')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@staff_member_required(login_url='/login/')
def promote_user_list(request):
    context = { 'users': User.objects.exclude(is_staff=True) }
    return render(request, 'list_users.html', context)


@staff_member_required(login_url='/login/')
def promote_user(request, username):
    user = User.objects.get(username=username)
    user.is_staff = True
    user.save()
    return redirect('/settings')
