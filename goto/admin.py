from django.contrib import admin
from goto.models import *

models = [Participant, Expert, Staff]
for model in models:
    admin.site.register(model)

# Register your models here.
