import requests
from django.conf import settings
from .models import *
from django.shortcuts import render
import hashlib


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
    #s = Subscriber.objects.get_or_create(email=email)
    mailchimp_subscribe(email)
    return render(req, 'index.html', {'info': 'Вы успешно подписаны на рассылку!'})


def unsubscribe(req):
    email = req.GET['email'].lower()
    #s = Subscriber.objects.filter(email=email)
    mailchimp_unsubscribe(email)
    return render(req, 'index.html', {'info': 'Вы успешно отписаны от рассылки!'})
