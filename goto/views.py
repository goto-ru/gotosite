from django.shortcuts import render
from django.http.response import HttpResponseServerError, HttpResponseRedirect

from django.contrib.auth import login, logout, authenticate
from goto.models import *
from django.contrib.auth.decorators import login_required
import datetime

from django.core.urlresolvers import reverse
from .forms import *


# Create your views here.


def index(req):
    context_dictionary = {}
    return render(req, 'index.html', context_dictionary)


def upcoming(req):
    events = Event.objects.filter(end_date__gte=datetime.date.today()).order_by('begin_date')
    return render(req, 'events.html', {'events': events, 'title': 'Ближайшие события'})


def archive(req):
    events = Event.objects.filter(end_date__lt=datetime.date.today()).order_by('-end_date')
    return render(req, 'events.html', {'events': events, 'title': 'Архив событий'})


def event_by_id(req, id):
    e = Event.objects.get(pk=id)
    return render(req, 'event_by_id.html', {'event': e})


def participants(req):
    participants = Participant.objects.all()
    return render(req, 'users.html', {'users': participants, 'title': 'Участники'})


def experts(req):
    experts = Expert.objects.all()

    return render(req, 'users.html', {'users': experts, 'title': 'Эксперты'})


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
        app.date_created = datetime.datetime.now()
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


@login_required()
def application(req, id):
    app = Application.objects.get(pk=id)
    base_context = {
    }
    if req.POST:
        if req.user.id == app.participant.id:
            if app.status == 1:
                if 'confirm' in req.POST:
                    app.status = 3
                    base_context['info'] = 'Заявка успешно подтвержденна'
                elif 'reject' in req.POST:
                    app.status = 4
                    base_context['info'] = 'Заявка успешно отозвана'
                app.save()
        else:
            base_context['err'] = 'You are not allowed to manage this application'
    base_context['application'] = app
    return render(req, 'application.html', base_context)


def render_profile_edit(req, user):
    user_form = UserEditForm(instance=user)
    base_context = {'user': user, 'user_form': user_form}
    if user.participant:
        participant_form = ParticipantEditForm(instance=user.participant)
        base_context['participant_form'] = participant_form
    return render(req, 'edit.html', base_context)

@login_required()
def profile_edit(req):
    user = GotoUser.objects.get(pk=req.user.pk)
    user_form = UserEditForm(req.POST, req.FILES or None)
    user_form.instance = user
    participant_form = ParticipantEditForm(req.POST, req.FILES or None)
    participant_form.instance = user
    if req.method == 'POST':

        if user_form.is_valid():
            # print(req.FILES['profile_picture'])
            # user.profile_picture = req.FILES['profile_picture']
            # user.save()
            # print(user.profile_picture)
            user_form.save()
        else:
            return render_profile_edit(req, user)
        if user.participant and participant_form.is_valid():
            participant_form.save()
        else:
            return render_profile_edit(req, user)

        return HttpResponseRedirect(reverse('user_detail', args=[user.id]))
    return render_profile_edit(req, user)


def about_us(req):
    return render(req, 'pages/about_us.html')

def hackathon(req):
    return render(req, 'pages/hackathon.html')

def school(req):
    return render(req, 'pages/school.html')

def intensive(req):
    return render(req, 'pages/intensive.html')

def lectoriy(req):
    return render(req, 'pages/lectoriy.html')

def page(req, slug):
    return render(req, 'pages/%s.html' % (slug,))


def user_by_id(req, id):
    user = GotoUser.objects.get(pk=id)
    return render(req, 'user_by_id.html', {'viewed_user': user})
