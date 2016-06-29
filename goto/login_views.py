from django.shortcuts import render
from django.http.response import HttpResponseServerError, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from goto.models import *
from django.contrib.auth.decorators import login_required


def sign_up(req):
    if req.POST:
        type = req.POST.get('type')
        password = req.POST.get('password')
        email = req.POST.get('email')

        if GotoUser.objects.filter(email=email).count() > 0:
            return render(req, 'signup.html', {'err': 'This email already exists!'})
        if type == 'participant':
            user = Participant()
        elif type == 'expert':
            user = Expert()
        else:
            return HttpResponseServerError()
        user.email = email
        user.username = email
        user.set_password(password)
        user.save()
        user_log = authenticate(username=email, password=password)
        login(req, user_log)
        return render(req, 'signup.html', {'info': "Successfully created!"})

    else:
        return render(req, 'signup.html')


def sign_in(req):
    if req.POST:
        password = req.POST.get('password')
        email = req.POST.get('email')
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(req, user)
                return render(req, 'login.html', {'info': 'Logged in!'})
            else:
                return render(req, 'login.html', {'err': 'Account is disabled'})
        else:
            return render(req, 'login.html', {'err': 'There is no such account'})
    else:
        return render(req, 'login.html')


@login_required
def sign_out(req):
    logout(req)
    return HttpResponseRedirect('/')
