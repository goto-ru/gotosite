from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseServerError, HttpResponseRedirect, HttpResponseForbidden

from django.contrib.auth import login, logout, authenticate
from goto.models import *
from django.contrib.auth.decorators import login_required
import datetime

from django.core.urlresolvers import reverse
from .forms import *
import requests
from django.contrib import messages


# Create your views here.


def index(req):
    s = Settings.objects.get()
    context_dictionary = {'partners': s.index_partners, 'articles': MassMediaArticle.objects.all()}
    return render(req, 'index.html', context_dictionary)


def mm_about(req):
    context_dictionary = {'articles': MassMediaArticle.objects.all()}
    return render(req, 'mm-articles.html', context_dictionary)


def upcoming(req):
    events = Event.objects.filter(end_date__gte=datetime.date.today()).order_by('begin_date')
    return render(req, 'events/events.html', {'events': events, 'title': 'Ближайшие события'})


def schools(req):
    events = Event.objects.filter(end_date__gte=datetime.date.today(), format='school').order_by('begin_date')
    return render(req, 'events/events.html', {'events': events, 'title': 'Школы'})


def hackathons(req):
    events = Event.objects.filter(end_date__gte=datetime.date.today(), format='hackathon').order_by('begin_date')
    return render(req, 'events/events.html', {'events': events, 'title': 'Хакатоны'})


def lectures(req):
    events = Event.objects.filter(end_date__gte=datetime.date.today(), format='lecture').order_by('begin_date')
    return render(req, 'events/events.html', {'events': events, 'title': 'Лекции'})


def archive(req):
    events = Event.objects.filter(end_date__lt=datetime.date.today()).order_by('-end_date')
    return render(req, 'events/events.html', {'events': events, 'title': 'Архив событий'})


def event_by_id(req, id):
    e = Event.objects.get(pk=id)
    base_context = {'event': e}
    try:
        p = req.user.gotouser.participant
    except AttributeError:
        p = None
    if p:
        a = p.application_set.filter(event=e)
        if a.count() > 0:
            base_context['application'] = a[0]
    return render(req, 'events/event_by_id.html', base_context)


def event_participants(req, id):
    e = Event.objects.get(pk=id)
    try:
        p = req.user.gotouser.participant
    except AttributeError:
        p = None
    if p:
        a = p.application_set.filter(event=e)
        if a.count() > 0 and (a[0].status == 1 or a[0].status == 3):

            base_context = {'event': e,
                            'invited': e.application_set.filter(status=1).all(),
                            'confirmed': e.application_set.filter(status=3).all()}
            return render(req, 'events/event_participants.html', base_context)
        else:
            return HttpResponseForbidden()


def participants(req):
    participants = Participant.objects.all()

    return render(req, 'user/users.html', {'users': participants, 'title': 'Участники'})


def experts(req):
    experts = Expert.objects.all()

    return render(req, 'user/users.html', {'users': experts, 'title': 'Эксперты'})


@login_required()
def application_fill(req, event_id):
    event = Event.objects.get(pk=event_id)
    base_cotext = {'event': event}
    if not req.user.is_authenticated():
        base_cotext['err'] = 'Пожалуйста, войдите как участник, чтобы подать заявку!'
        return render(req, 'events/events.html', base_cotext)
    user = GotoUser.objects.get(pk=req.user.pk)
    base_cotext['user'] = user
    if user.participant is None:
        base_cotext.update({'err': 'Пожалуйста, '
                                   'войдите как участник, чтобы подать заявку!'})
        return render(req, 'fill_application.html', base_cotext)
    a = Application.objects.filter(participant=user.participant, event=event)
    if a.count() > 0:
        base_cotext.update({'err': 'Вы уже отправили заявку. Посмотреть статус можно в личном кабинете.'})
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


def project_by_id(req, id):
    project = Project.objects.get(pk=id)
    base_context = {'project': project}
    return render(req, 'project_by_id.html', base_context)


@login_required()
def project_create(req, ):
    if req.POST:
        project_form = ProjectEditForm(req.POST)
        project_form.save()
        return HttpResponseRedirect(reverse('project_detail', args=[project_form.instance.id]))
    else:
        project_form = ProjectEditForm()
        return render(req, 'project_create.html', {'project_form': project_form})


@login_required()
def project_edit(req, id):
    project = Project.objects.get(pk=id)
    if not (req.user.gotouser.participant and req.user.gotouser.participant in project.maintainers.all()):
        messages.error(req, 'У вас недостаточно прав для изменения этого проекта')
        return HttpResponseRedirect(reverse('project_detail', args=[project.id]))
    if req.POST:
        project_form = ProjectEditForm(req.POST)
        project_form.instance = project
        project_form.save()
        messages.info(req, 'Изменения внесены')
        return HttpResponseRedirect(reverse('project_detail', args=[project.id]))
    else:
        project_form = ProjectEditForm(instance=project)
        return render(req, 'project_edit.html', {'project_form': project_form,
                                                 'project': project})


@login_required()
def project_delete(req, id):
    project = Project(pk=id)
    if not (req.user.gotouser.participant and req.user.gotouser.participant in project.maintainers.all()):
        messages.error(req, 'У вас недостаточно прав для удаления этого проекта')
        return HttpResponseRedirect(reverse('project_detail', args=[project.id]))
    project.delete()
    messages.info(req, 'Успешо удалено')
    return HttpResponseRedirect(reverse('user_detail', args=[req.user.id]))


def projects(req):
    projects = Project.objects.all()
    return render(req, 'projects.html', {'projects': projects})


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
    return render(req, 'user/edit.html', base_context)


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
    s = Settings.objects.get()
    context_dictionary = {'partners': s.about_us_partners, 'team': s.about_us_team}
    return render(req, 'about.html', context_dictionary)


def info(req):
    return render(req, 'info.html', {})


def page(req, slug):
    return render(req, 'pages/%s.html' % (slug,))


def user_by_id(req, id):
    user = GotoUser.objects.get(pk=id)
    base_context = {'viewed_user': user}
    # comments = None
    try:
        if user.participant:
            if req.user.has_perm('view_private_comment'):
                base_context['private_comments'] = user.participant.comments.filter(is_private=True)
            else:
                base_context['public_comments'] = user.participant.comments.filter(is_private=False)
    except user.DoesNotExist:
        pass
    # acc should be typeB if account only has typeA and typeB subclasses

    return render(req, 'user/user_by_id.html', base_context)


def assignment(req, id):
    """view assignment"""
    assignment = get_object_or_404(Assignment, pk=id)
    base_context = {'assignment': assignment}
    if req.user.gotouser.participant:
        base_context['solutions'] = Solution.objects.filter(assignment=assignment,
                                                            participant=req.user.gotouser.participant).all()
    return render(req, 'solution/assignment.html', base_context)


@login_required()
def apply_solution(req, id):
    """Only participants"""
    if req.POST:
        participant = get_object_or_404(Participant, pk=req.user.pk)
        s = Solution()
        if req.FILES:
            s.file = req.FILES['file']
        s.participant_comment = req.POST['comment']
        s.participant = participant
        s.assignment = get_object_or_404(Assignment, id=id)
        s.date_posted = datetime.datetime.now()
        s.save()
    return HttpResponseRedirect(reverse('assignment', args=[id]))


def view_solution(req, id):
    solution = get_object_or_404(Solution, pk=id)
    return render(req, 'solution/solution.html', {'solution': solution})
