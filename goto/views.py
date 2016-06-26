from django.shortcuts import render
from django.http.response import HttpResponseServerError, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from goto.models import *
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.

def index(req):
    context_dictionary = {}
    return render(req, 'index.html', context_dictionary)


def upcoming(req):
    events = Event.objects.filter(end_date__gte=datetime.date.today()).order_by('begin_date')
    return render(req, 'events.html', {'events': events})

def archive(req):
    events = Event.objects.filter(end_date__lte =datetime.date.today()).order_by('-end_date')
    return render(req, 'events.html', {'events': events})


def event_by_id(req, id):
    e = Event.objects.get(pk=id)
    return render(req, 'event_by_id.html', {'event': e})


def participants(req):
    participants = Participant.objects.all()
    return render(req, 'users.html', {'users': participants})


def experts(req):
    pass


def user_by_id(req, id):
    user = User.objects.get(pk=id)
    return render(req, 'user_by_id.html', {'user': user})
