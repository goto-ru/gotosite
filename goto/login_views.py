from django.shortcuts import render
from django.http.response import HttpResponseServerError, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from goto.models import *
from django.contrib.auth.decorators import login_required

from django.core.urlresolvers import reverse

from django.contrib import messages


def sign_up(req):
    if req.POST:
        type = req.POST.get('type')
        password = req.POST.get('password')
        email = req.POST.get('email')

        if GotoUser.objects.filter(email=email).count() > 0:
            messages.error(req, 'Email уже зарегестрирован!')
            return render(req, 'signup.html')
        if type == 'participant':
            user = Participant()
        elif type == 'expert':
            user = Expert()
        else:
            return HttpResponseServerError()
        user.email = email
        if type == 'participant':
            user.subscribed_to_email = True
        user.username = email
        user.first_name = req.POST['first_name']
        user.last_name = req.POST['last_name']

        user.set_password(password)
        user.save()
        user_log = authenticate(username=email, password=password)
        login(req, user_log)
        messages.info(req, 'Аккаунт успешно создан')
        return HttpResponseRedirect(reverse('user_detail', args=[user.id]))


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
                return HttpResponseRedirect(reverse('user_detail', args=[user.id]))
            else:

                messages.error(req, 'Аккаунт отключен')
                return render(req, 'login.html')
        else:
            messages.error(req, 'Нет такого аккаунта')
            return render(req, 'login.html')
    else:
        return render(req, 'login.html')


@login_required
def sign_out(req):
    logout(req)
    return HttpResponseRedirect('/')
