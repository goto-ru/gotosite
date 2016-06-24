from django.shortcuts import render

from goto.models import *
# Create your views here.

def index(request):
    context_dictionary = {}

    return render(request, 'index.html', context_dictionary)