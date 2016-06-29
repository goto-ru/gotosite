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
    events = Event.objects.filter(end_date__lt=datetime.date.today()).order_by('-end_date')
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


def profile(req):
    if req.user.is_authenticated():
        user = GotoUser.objects.get(pk=req.user.pk)
        return render(req, 'profile.html', {'user': user})
    else:
        return HttpResponseRedirect('/signin')


def application_fill(req, event_id):
    user = GotoUser.objects.get(pk=req.user.pk)
    event = Event.objects.get(pk=event_id)
    base_cotext = {'user': user, 'event': event}
    if not user.is_authenticated() or user.participant is None:
        base_cotext.update({'err': 'Please login as participant to fill application!'})
        return render(req, 'fill_application.html', base_cotext)
    a = Application.objects.filter(participant=user.participant, event=event)
    if a.count() > 0:
        base_cotext.update({'err': 'You already posted an application!'})
        return render(req, 'fill_application.html', base_cotext)
    if req.method == 'POST':
        app = Application()
        app.event = event
        app.participant = user.participant
        app.save()

        for q in event.questions.all():
            text = req.POST['question%s' % q.pk]
            ans = Answer()
            ans.application = app
            ans.question = q
            ans.text = text
            ans.save()
        base_cotext.update({'info': 'Successfully accepted!'})
        return render(req, 'fill_application.html', base_cotext)
    else:
        return render(req, 'fill_application.html', base_cotext)


def application(req, id):
    pass


def profile_edit(req):
    user = GotoUser.objects.get(pk=req.user.pk)
    form = ProfileEditForm(req.POST or None, req.FILES or None, instance=user)
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
    return render(req, 'pages/%s.html' % (slug, ))


def user_by_id(req, id):
    user = GotoUser.objects.get(pk=id)
    return render(req, 'user_by_id.html', {'user': user})
