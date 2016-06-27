from django.shortcuts import render
from django.http.response import HttpResponseServerError, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from goto.models import *
from django.contrib.auth.decorators import login_required
import datetime

from .forms import *


# Create your views here.

def index(req):
    context_dictionary = {}
    return render(req, 'index.html', context_dictionary)


def upcoming(req):
    events = Event.objects.filter(end_date__gte=datetime.date.today()).order_by('begin_date')
    return render(req, 'events.html', {'events': events})


def archive(req):
    events = Event.objects.filter(end_date__lte=datetime.date.today()).order_by('-end_date')
    return render(req, 'events.html', {'events': events})


def event_by_id(req, id):
    e = Event.objects.get(pk=id)
    return render(req, 'event_by_id.html', {'event': e})


def participants(req):
    participants = Participant.objects.all()
    return render(req, 'users.html', {'users': participants})


def experts(req):
    experts = Expert.objects.all()
    return render(req, 'users.html', {'users': experts})


def staff(req):
    staff = Staff.objects.all()
    return render(req, 'users.html', {'users': staff})


def profile(req):
    if req.user.is_authenticated():
        user = GotoUser.objects.get(pk=req.user.pk)
        return render(req, 'profile.html', {'user': user})
    else:
        return HttpResponseRedirect('/signin')


def profile_edit(req):
    user = GotoUser.objects.get(pk=req.user.pk)
    form = ProfileEditForm(req.POST or None, instance=user)
    if req.method == 'POST':
        # create a form instance and populate it with data from the request:

        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profile')
        else:
            pass
    # if a GET (or any other method) we'll create a blank form
    else:
        pass
    return render(req, 'edit.html', {'user': user, 'form': form})


def about_us(req):
    pass


def page(req, slug):
    return render(req, 'pages/%s.html' % (slug,))


def user_by_id(req, id):
    user = GotoUser.objects.get(pk=id)
    return render(req, 'user_by_id.html', {'user': user})
