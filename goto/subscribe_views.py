import requests
from django.conf import settings
from .models import *
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
import hashlib
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required




def mailchimp_subscribe(email):
    send_json = {'status': 'subscribed',
                 'email_address': email}
    resp = requests.post('https://us13.api.mailchimp.com/3.0/lists/%s/members' % settings.MAILCHIMP_LIST_ID,
                         json=send_json, auth=('dummystring', settings.MAILCHIMP_API_KEY))


def mailchimp_unsubscribe(email):
    email_hash = hashlib.md5(email.encode()).hexdigest()
    send_json = {'status': 'unsubscribed'}
    resp = requests.delete('https://us13.api.mailchimp.com/3.0/lists/%s/members/%s' %
                           (settings.MAILCHIMP_LIST_ID, email_hash), json=send_json,
                           auth=('dummystring', settings.MAILCHIMP_API_KEY))


def subscribe(req):
    email = req.GET['email'].lower()
    # s = Subscriber.objects.get_or_create(email=email)
    mailchimp_subscribe(email)
    messages.info(req, 'Вы успешно подписаны на рассылку!')
    return HttpResponseRedirect('/')


def unsubscribe(req):
    email = req.GET['email'].lower()
    # s = Subscriber.objects.filter(email=email)
    mailchimp_unsubscribe(email)
    messages.info(req, 'Вы успешно отписаны от рассылки!')
    return HttpResponseRedirect('/')

@staff_member_required
def ask_for_email(req, emails):

    if req.POST:
        topic = req.POST['topic']
        text = req.POST['text']
        send_mail(topic, text, settings.EMAIL_FROM, emails.split(','))
        return HttpResponseRedirect('/admin/goto/application/')
    else:
        return render(req, 'email_ask.html', {'emails': emails})

