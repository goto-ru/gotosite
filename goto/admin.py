from django.contrib import admin
from goto.models import *

models = [Participant, Expert, Staff, Page, Answer, Question]


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0
    max_num = 0

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    model = Event
    #inlines = [QuestionInline]



for model in models:
    admin.site.register(model)
1

# Register your models here.
